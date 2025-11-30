# Dynamic Resume API (Flask + Templates + Embeddings)

This project exposes a simple Flask API that generates a tailored resume
(HTML or Markdown) given:

- `candidate_profile` JSON
- raw `job_description` text
- `template_id` (1, 2, or 3)

It uses `sentence-transformers` to rank candidate bullets vs JD and Jinja2
templates to render HTML/Markdown.
