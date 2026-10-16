import re

def parse_jobs(markdown: str) -> list[dict]:
    """Convert HiringCafe's markdown response into job dictionaries."""

    jobs = []

    # Each job starts with a markdown heading containing its title.
    sections = re.split(r"(?=^### )", markdown, flags=re.MULTILINE)

    for section in sections:
        title_match = re.search(
            r"^### \[(.*?)\]\((.*?)\)",
            section,
            flags=re.MULTILINE
        )

        if not title_match:
            continue

        title, url = title_match.groups()

        def extract(pattern: str) -> str | None:
            match = re.search(pattern, section, flags=re.MULTILINE)
            return match.group(1).strip() if match else None

        company = extract(r"^\*\*(.+?)\*\*\s*$")
        location = extract(r"^- \*\*Location:\*\* (.*)$")
        workplace = extract(r"^- \*\*Workplace:\*\* (.*)$")
        compensation = extract(r"^- \*\*Compensation:\*\* (.*)$")
        employment_type = extract(r"^- \*\*Employment type:\*\* (.*)$")
        seniority = extract(r"^- \*\*Seniority:\*\* (.*)$")
        posted = extract(r"^- \*\*Posted:\*\* (.*)$")
        job_id = extract(r"^- \*\*Job ID:\*\* (.*)$")

        jobs.append({
            "title" : title,
            "url" : url,
            "company": company,
            "location": location,
            "workplace": workplace,
            "compensation": compensation,
            "employment_type": employment_type,
            "seniority": seniority,
            "posted": posted,
            "job_id": job_id
        })

    return jobs