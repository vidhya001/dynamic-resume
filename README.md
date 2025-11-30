# Dynamic Resume API (Flask + Templates + Embeddings)

Dynamic Resume API is a small ML-powered service that generates **JD-tailored resumes** from a candidate profile and a job description. It uses:

- **Flask** – REST API
- **Sentence Transformers** – to rank the most relevant bullets (semantic matching)
- **Jinja2 templates** – to render different resume layouts (HTML/Markdown)

---

## Features

- 🔁 **JD-aware bullet selection** using embeddings (`all-MiniLM-L6-v2`)
- 🧩 **Multiple templates** (classic, two-column, senior)
- 📄 Output as **HTML** or **Markdown**
- ⚙️ Simple REST API – easy to plug into any frontend or CLI

---

## Quickstart

```bash
git clone https://github.com/your-user/dynamic-resume-api.git
cd dynamic-resume-api

python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python app.py
# API runs at http://127.0.0.1:5000
