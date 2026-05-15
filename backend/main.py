"""
LexAfrica AI — FastAPI Backend
4-agent pipeline: Intake → Research → Advisor → Document
Powered by Qwen2.5-72B on AMD Instinct MI300X
"""

import os, json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from utils.pdf_generator import generate_pdf
import uvicorn

load_dotenv()

app = FastAPI(title="LexAfrica AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Groq LLM ─────────────────────────────────────────────────────────────────
def get_llm(temperature=0.3):
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model=os.getenv("GROQ_MODEL"),
        temperature=temperature,
    )

# ── Request / Response schemas ───────────────────────────────────────────────
class LegalQuery(BaseModel):
    problem: str
    country: str = "Nigeria"
    language: str = "English"

class LegalResponse(BaseModel):
    domain: str
    rights: list[str]
    advice: str
    next_steps: list[str]
    legal_letter: str
    disclaimer: str

# ── Agent 1: INTAKE — classify the legal domain ──────────────────────────────
def intake_agent(problem: str, country: str) -> dict:
    llm = get_llm(temperature=0.1)
    messages = [
        SystemMessage(content="""You are a legal intake specialist for African law.
Classify the user's legal problem into exactly one domain.
Respond ONLY with valid JSON, no markdown, no extra text.
Format: {"domain": "...", "sub_domain": "...", "urgency": "low|medium|high", "keywords": [...]}
Domains: Tenancy, Employment, Contract, Criminal, Family, Land/Property, Consumer Rights, Human Rights, Immigration, Business/Corporate"""),
        HumanMessage(content=f"Country: {country}\nProblem: {problem}")
    ]
    res = llm.invoke(messages)
    return json.loads(res.content.strip())

# ── Agent 2: RESEARCH — pull relevant laws & rights ──────────────────────────
def research_agent(problem: str, intake: dict, country: str) -> dict:
    llm = get_llm(temperature=0.2)
    messages = [
        SystemMessage(content=f"""You are an expert in {country} law and pan-African legal frameworks.
Given the legal domain and user problem, return relevant laws, rights, and precedents.
Respond ONLY with valid JSON, no markdown.
Format: {{
  "applicable_laws": ["law 1", "law 2"],
  "user_rights": ["right 1", "right 2"],
  "relevant_bodies": ["body 1"],
  "time_limits": "any deadlines the user must know about"
}}"""),
        HumanMessage(content=f"Domain: {intake['domain']}\nSub-domain: {intake['sub_domain']}\nProblem: {problem}")
    ]
    res = llm.invoke(messages)
    return json.loads(res.content.strip())

# ── Agent 3: ADVISOR — plain language advice + next steps ────────────────────
def advisor_agent(problem: str, intake: dict, research: dict, country: str) -> dict:
    llm = get_llm(temperature=0.4)
    messages = [
        SystemMessage(content=f"""You are a compassionate legal advisor helping everyday citizens in {country}.
Write clear, plain-language advice. Avoid legal jargon.
Respond ONLY with valid JSON, no markdown.
Format: {{
  "summary": "2-3 sentence plain summary of their situation",
  "advice": "detailed practical advice paragraph",
  "next_steps": ["step 1", "step 2", "step 3"],
  "warning": "any important caution"
}}"""),
        HumanMessage(content=f"""Problem: {problem}
Domain: {intake['domain']} — Urgency: {intake['urgency']}
Rights: {json.dumps(research['user_rights'])}
Laws: {json.dumps(research['applicable_laws'])}""")
    ]
    res = llm.invoke(messages)
    return json.loads(res.content.strip())

# ── Agent 4: DOCUMENT — generate a formal legal letter ───────────────────────
def document_agent(problem: str, intake: dict, advisor: dict, country: str) -> str:
    llm = get_llm(temperature=0.3)
    messages = [
        SystemMessage(content=f"""You are a legal document drafter for {country}.
Write a formal legal letter the user can send to the relevant party or authority.
Use proper legal letter format with [SENDER NAME], [DATE], [RECIPIENT] placeholders.
The letter should be firm, professional, and cite the relevant legal basis.
Return ONLY the letter text, no JSON, no extra commentary."""),
        HumanMessage(content=f"""Problem: {problem}
Domain: {intake['domain']}
Next steps: {json.dumps(advisor['next_steps'])}
Advice summary: {advisor['summary']}""")
    ]
    res = llm.invoke(messages)
    return res.content.strip()

# ── Main pipeline endpoint ────────────────────────────────────────────────────
@app.post("/api/analyze", response_model=LegalResponse)
async def analyze(query: LegalQuery):
    try:
        # Run the 4-agent pipeline sequentially
        intake   = intake_agent(query.problem, query.country)
        research = research_agent(query.problem, intake, query.country)
        advisor  = advisor_agent(query.problem, intake, research, query.country)
        letter   = document_agent(query.problem, intake, advisor, query.country)

        return LegalResponse(
            domain=f"{intake['domain']} — {intake.get('sub_domain', '')}",
            rights=research.get("user_rights", []),
            advice=advisor.get("advice", ""),
            next_steps=advisor.get("next_steps", []),
            legal_letter=letter,
            disclaimer="This is AI-generated legal information, not legal advice. "
                       "Consult a qualified lawyer for your specific situation."
        )
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Agent parsing error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── PDF download endpoint ─────────────────────────────────────────────────────
@app.post("/api/download-pdf")
async def download_pdf(data: LegalResponse):
    from fastapi.responses import StreamingResponse
    import io
    pdf_bytes = generate_pdf(data.dict())
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=lexafrica-legal-report.pdf"}
    )

@app.get("/")
def root():
    return {"status": "LexAfrica AI is running", "model": os.getenv("AMD_MODEL")}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)