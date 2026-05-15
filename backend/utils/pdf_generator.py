from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import cm
import io
from datetime import datetime

PRIMARY  = HexColor("#1a1a2e")
ACCENT   = HexColor("#e94560")
GRAY     = HexColor("#6b7280")

def generate_pdf(data: dict) -> bytes:
    buf_io = io.BytesIO()
    doc = SimpleDocTemplate(buf_io, pagesize=A4,
        topMargin=2*cm, bottomMargin=2*cm,
        leftMargin=2.5*cm, rightMargin=2.5*cm)

    story = []

    title_style  = ParagraphStyle("title", fontSize=22, textColor=PRIMARY, spaceAfter=4, fontName="Helvetica-Bold")
    sub_style    = ParagraphStyle("sub", fontSize=10, textColor=GRAY, spaceAfter=2)
    h2_style     = ParagraphStyle("h2", fontSize=13, textColor=PRIMARY, spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold")
    body_style   = ParagraphStyle("body", fontSize=10, textColor=PRIMARY, leading=16, spaceAfter=8)
    bullet_style = ParagraphStyle("bullet", fontSize=10, textColor=PRIMARY, leading=15, leftIndent=16, spaceAfter=4)
    disc_style   = ParagraphStyle("disc", fontSize=8, textColor=GRAY, leading=12, spaceBefore=8)

    story.append(Paragraph("LexAfrica AI", title_style))
    story.append(Paragraph("Legal Intelligence Report", sub_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}", sub_style))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=16))

    story.append(Paragraph("Legal Domain", h2_style))
    story.append(Paragraph(f"<b>{data.get('domain', 'N/A')}</b>", body_style))

    story.append(Paragraph("Your Rights", h2_style))
    for r in data.get("rights", []):
        story.append(Paragraph(f"• {r}", bullet_style))

    story.append(Paragraph("Legal Advice", h2_style))
    story.append(Paragraph(data.get("advice", ""), body_style))

    story.append(Paragraph("Recommended Next Steps", h2_style))
    for i, step in enumerate(data.get("next_steps", []), 1):
        story.append(Paragraph(f"{i}. {step}", bullet_style))

    story.append(Paragraph("Formal Legal Letter", h2_style))
    for line in data.get("legal_letter", "").split("\n"):
        story.append(Paragraph(line or "&nbsp;", body_style))

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=1, color=GRAY))
    story.append(Paragraph(f"DISCLAIMER: {data.get('disclaimer', '')}", disc_style))

    doc.build(story)
    return buf_io.getvalue()