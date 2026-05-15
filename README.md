# ⚖️ LexAfrica AI
### Legal Intelligence for Every African Citizen

> **4 specialized AI agents** analyze your legal problem, find your rights, and draft a formal letter — **in seconds, in any language, via voice or text.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hackathon](https://img.shields.io/badge/Hackathon-AI%20Agent%20Olympics-red)](https://lablab.ai/event/ai-agent-olympics-hackathon)

---

## 🌍 The Problem

**1.4 billion Africans** lack access to legal services. Legal help costs $100-500 per consultation — **unaffordable for 85% of the population**. Language barriers, low literacy, and geographic isolation make it worse.

**Result:** People lose their rights, get exploited, and have no recourse.

---

## 💡 Our Solution

**LexAfrica AI** democratizes legal access through **4 autonomous AI agents** that work together:

### 🔍 Agent 1: Intake Agent
- Classifies legal domain (Tenancy, Employment, Contract, etc.)
- Assesses urgency level
- Extracts key facts

### 📚 Agent 2: Research Agent
- Finds applicable laws for the user's country
- Identifies user's legal rights
- Locates relevant legal bodies and time limits

### ⚖️ Agent 3: Advisor Agent
- Provides plain-language legal advice
- Explains options clearly
- Gives actionable next steps

### 📝 Agent 4: Document Agent
- Drafts a formal legal letter
- Cites relevant laws
- Ready to send to landlords, employers, etc.

---

## ✨ Key Features

### 🎤 Voice Input
- Speak your legal problem in any language
- Perfect for low-literacy users
- Powered by Speechmatics real-time transcription

### 🌐 Multi-Language Support
- English, Swahili, Hausa, Yoruba, French, Amharic
- AI responds in user's preferred language
- Expanding to 20+ African languages

### 📄 Instant Legal Documents
- Download professional PDF reports
- Formal legal letters ready to send
- Includes all rights and next steps

### 🚀 Real-Time Agent Visualization
- Watch agents work together
- See the decision-making process
- Full transparency in AI reasoning

---

## 🛠️ Technology Stack

- **AI Model:** Llama 3.3 70B (via Groq)
- **Agent Framework:** LangChain + Custom orchestration
- **Voice:** Speechmatics real-time ASR
- **Backend:** FastAPI (Python)
- **Frontend:** Next.js 15 + TypeScript
- **Deployment:** Render + Vercel

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Groq API key

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "GROQ_API_KEY=your_key_here" > .env
echo "GROQ_MODEL=llama-3.3-70b-versatile" >> .env

# Run server
python main.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000`

---

## 📊 Impact Metrics

- **Target Users:** 1.4 billion Africans
- **Cost Reduction:** From $100-500 to **FREE**
- **Time Reduction:** From days/weeks to **30 seconds**
- **Languages:** 6 (expanding to 20+)
- **Accessibility:** Voice input for low-literacy users

---

## 🏆 Hackathon Prizes Targeted

1. **Featherless Prize** - Domain-specialized legal agent
2. **Speechmatics Prize** - Voice-powered legal assistance
3. **Google Gemini Prize** - Best autonomous agent system
4. **Vultr Prize** - Production deployment

---

## 🎯 Business Model

### Freemium
- Basic legal advice: **Free**
- Premium: Lawyer connections, court filing assistance

### B2B Partnerships
- NGOs and legal aid organizations
- Government legal aid programs
- Microfinance institutions

### Revenue Projections
- Year 1: 100K users → $50K revenue
- Year 3: 5M users → $2.5M revenue

---

## 🔮 Roadmap

### Phase 1 (Current)
- ✅ 4-agent pipeline
- ✅ Multi-language support
- ✅ Voice input UI
- ✅ PDF generation

### Phase 2 (Next 3 months)
- [ ] Speechmatics full integration
- [ ] SMS/WhatsApp bot
- [ ] 20+ African languages
- [ ] Lawyer marketplace

### Phase 3 (6-12 months)
- [ ] Court document filing
- [ ] Legal case tracking
- [ ] Community legal forums
- [ ] Mobile apps (iOS/Android)

---

## 👥 Team

**Sadiq Haruna** - Full-stack AI Engineer
- Building AI solutions for Africa
- Passionate about access to justice

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- **Groq** for lightning-fast inference
- **Speechmatics** for voice technology
- **lablab.ai** for the hackathon platform
- **AI Agent Olympics** for the opportunity

---

## 📞 Contact

- **Demo:** [Coming soon]
- **GitHub:** https://github.com/Charly070321/LexAfrica-AI
- **Email:** [Your email]

---

<div align="center">

**Built with ❤️ for Africa at AI Agent Olympics Hackathon 2026**

*Democratizing legal access, one AI agent at a time.*

</div>
