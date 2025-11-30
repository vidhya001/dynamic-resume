from flask import Flask, request, jsonify, Response

from parser import jd_text_to_sections
from matcher import rank_bullets_for_jd
from flask_cors import CORS
from generator import render_resume_markdown, render_resume_html

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

TEMPLATES = {
    1: "Classic single-column",
    2: "Two-column with sidebar",
    3: "Senior banner style",
}


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/templates", methods=["GET"])
def list_templates():
    templates = [
        {"template_id": tid, "name": desc}
        for tid, desc in sorted(TEMPLATES.items())
    ]
    return jsonify({"templates": templates})


@app.route("/generate-resume", methods=["POST"])
def generate_resume():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    candidate_profile = data.get("candidate_profile")
    job_description = data.get("job_description")

    if not candidate_profile or not job_description:
        return jsonify({
            "error": "Both 'candidate_profile' and 'job_description' are required"
        }), 400

    template_id = data.get("template_id", 1)
    if template_id not in TEMPLATES:
        template_id = 1

    top_k = data.get("top_k", 10)
    output_format = str(data.get("output_format", "html")).lower()

    jd_sections = jd_text_to_sections(job_description)
    selected_bullets = rank_bullets_for_jd(
        jd_sections=jd_sections,
        profile=candidate_profile,
        top_k=top_k,
    )

    if output_format in ("md", "markdown"):
        content = render_resume_markdown(
            profile=candidate_profile,
            selected_bullets=selected_bullets,
            template_id=template_id,
        )
        mimetype = "text/markdown; charset=utf-8"
    else:
        content = render_resume_html(
            profile=candidate_profile,
            selected_bullets=selected_bullets,
            template_id=template_id,
        )
        mimetype = "text/html; charset=utf-8"

    return Response(content, mimetype=mimetype)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
