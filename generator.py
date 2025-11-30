from typing import Dict, Any, List, Tuple
from pathlib import Path
from collections import defaultdict

from jinja2 import Environment, FileSystemLoader


def _create_env() -> Environment:
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    return env


def _group_bullets_by_role(selected_bullets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str, str, str], List[str]] = defaultdict(list)
    for b in selected_bullets:
        key = (
            b.get("company", ""),
            b.get("title", ""),
            b.get("location", ""),
            b.get("start", ""),
            b.get("end", ""),
        )
        grouped[key].append(b.get("bullet", ""))

    experience: List[Dict[str, Any]] = []
    for (company, title, location, start, end), bullets in grouped.items():
        experience.append(
            {
                "company": company,
                "title": title,
                "location": location,
                "start": start,
                "end": end,
                "bullets": bullets,
            }
        )

    experience.sort(key=lambda e: e.get("start", ""), reverse=True)
    return experience


def render_resume_markdown(
    profile: Dict[str, Any],
    selected_bullets: List[Dict[str, Any]],
    template_id: int,
) -> str:
    env = _create_env()
    template_map = {
        1: "template1_classic.md.j2",
        2: "template2_twocol.md.j2",
        3: "template3_senior.md.j2",
    }
    template_file = template_map.get(template_id, "template1_classic.md.j2")
    tmpl = env.get_template(template_file)

    experience = _group_bullets_by_role(selected_bullets)
    rendered = tmpl.render(
        profile=profile,
        summary=profile.get("summary", ""),
        experience=experience,
        education=profile.get("education", []),
        skills=profile.get("skills", []),
        extra=profile.get("extra", []),
    )
    return rendered


def render_resume_html(
    profile: Dict[str, Any],
    selected_bullets: List[Dict[str, Any]],
    template_id: int,
) -> str:
    env = _create_env()
    template_map = {
        1: "template1_classic.html.j2",
        2: "template2_twocol.html.j2",
        3: "template3_senior.html.j2",
    }
    template_file = template_map.get(template_id, "template1_classic.html.j2")
    tmpl = env.get_template(template_file)

    experience = _group_bullets_by_role(selected_bullets)
    rendered = tmpl.render(
        profile=profile,
        summary=profile.get("summary", ""),
        experience=experience,
        education=profile.get("education", []),
        skills=profile.get("skills", []),
        extra=profile.get("extra", []),
    )
    return rendered
