import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

with open("src/llm-concepts-persian.md", "r", encoding="utf-8") as f:
    md_content = f.read()

html_body = markdown.markdown(
    md_content,
    extensions=["tables", "fenced_code", "toc"]
)

html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

  * {{ box-sizing: border-box; }}

  body {{
    font-family: 'Vazirmatn', 'Tahoma', 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 13px;
    line-height: 2;
    color: #1a1a2e;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }}

  .page {{
    max-width: 100%;
    padding: 40px 50px;
  }}

  h1 {{
    font-size: 26px;
    color: #0f3460;
    border-bottom: 3px solid #e94560;
    padding-bottom: 10px;
    margin-bottom: 20px;
    text-align: center;
  }}

  h2 {{
    font-size: 18px;
    color: #16213e;
    background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 6px;
    margin-top: 30px;
    margin-bottom: 14px;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 15px;
    color: #0f3460;
    border-right: 4px solid #e94560;
    padding-right: 10px;
    margin-top: 18px;
  }}

  p {{
    margin: 8px 0;
    text-align: justify;
  }}

  code {{
    font-family: 'Courier New', monospace;
    direction: ltr;
    text-align: left;
    background: #f0f4ff;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 11px;
    color: #c7254e;
  }}

  pre {{
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 14px 16px;
    border-radius: 8px;
    direction: ltr;
    text-align: left;
    font-family: 'Courier New', monospace;
    font-size: 11px;
    overflow: hidden;
    white-space: pre-wrap;
    word-break: break-word;
    margin: 12px 0;
    border-right: 4px solid #e94560;
    page-break-inside: avoid;
  }}

  pre code {{
    background: none;
    color: inherit;
    padding: 0;
    font-size: 11px;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 12px;
    page-break-inside: avoid;
  }}

  th {{
    background: #0f3460;
    color: white;
    padding: 8px 12px;
    text-align: right;
    font-weight: bold;
  }}

  td {{
    padding: 7px 12px;
    border-bottom: 1px solid #e0e6f0;
    text-align: right;
  }}

  tr:nth-child(even) td {{
    background: #f8f9ff;
  }}

  blockquote {{
    border-right: 4px solid #e94560;
    margin: 14px 0;
    padding: 10px 16px;
    background: #f8f9ff;
    color: #444;
    font-style: italic;
  }}

  ul, ol {{
    padding-right: 24px;
    padding-left: 0;
    margin: 8px 0;
  }}

  li {{
    margin: 4px 0;
    line-height: 1.9;
  }}

  hr {{
    border: none;
    border-top: 2px solid #e0e6f0;
    margin: 24px 0;
  }}

  strong {{
    color: #0f3460;
    font-weight: bold;
  }}

  em {{
    color: #555;
  }}

  @page {{
    size: A4;
    margin: 15mm 15mm 18mm 15mm;
    @bottom-center {{
      content: counter(page);
      font-size: 11px;
      color: #888;
    }}
  }}
</style>
</head>
<body>
<div class="page">
{html_body}
</div>
</body>
</html>"""

font_config = FontConfiguration()
css = CSS(string="", font_config=font_config)

HTML(string=html, base_url=".").write_pdf(
    "llm-concepts-persian.pdf",
    font_config=font_config
)

print("PDF created: llm-concepts-persian.pdf")
