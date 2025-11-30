from typing import List, Dict, Any


def jd_text_to_sections(jd_text: str) -> Dict[str, List[str]]:
    lines = [line.strip() for line in jd_text.splitlines() if line.strip()]

    responsibilities: List[str] = []
    requirements: List[str] = []
    other: List[str] = []

    current_section = "other"

    for line in lines:
        lower = line.lower()
        if "responsibilities" in lower:
            current_section = "responsibilities"
            continue
        elif "requirements" in lower:
            current_section = "requirements"
            continue

        if line.startswith("-") or line.startswith("*"):
            content = line.lstrip("-*").strip()
            if current_section == "responsibilities":
                responsibilities.append(content)
            elif current_section == "requirements":
                requirements.append(content)
            else:
                other.append(content)
        else:
            other.append(line)

    return {
        "responsibilities": responsibilities,
        "requirements": requirements,
        "other": other,
    }


def extract_candidate_bullets(profile: Dict[str, Any]) -> List[Dict[str, str]]:
    bullets: List[Dict[str, str]] = []

    for exp in profile.get("experience", []):
        for b in exp.get("bullets", []):
            bullets.append(
                {
                    "company": exp.get("company", ""),
                    "title": exp.get("title", ""),
                    "location": exp.get("location", ""),
                    "start": exp.get("start", ""),
                    "end": exp.get("end", ""),
                    "bullet": b,
                    "source": "experience",
                }
            )

    for extra in profile.get("extra", []):
        bullets.append(
            {
                "company": "Extra",
                "title": "Other",
                "location": "",
                "start": "",
                "end": "",
                "bullet": extra,
                "source": "extra",
            }
        )

    return bullets


def jd_sections_to_sentences(sections: Dict[str, List[str]]) -> List[str]:
    sentences: List[str] = []
    for key in ["responsibilities", "requirements", "other"]:
        sentences.extend(sections.get(key, []))
    return sentences
