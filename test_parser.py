from job_parser import parse_jobs

sample = """
## HiringCafe job results

### [AI PhD ML Engineering Intern](https://example.com/job/123)
**Eli Lilly and Company**
- **Location:** Indianapolis, Indiana, United States
- **Workplace:** Onsite
- **Compensation:** $119,850 – $136,000/yr
- **Employment type:** Full Time, Internship
- **Seniority:** Entry Level
- **Posted:** 2026-09-04
- **Job ID:** abc123

A sample job description.
"""


jobs = parse_jobs(sample)

assert len(jobs) == 1
assert jobs[0]["company"] == "Eli Lilly and Company"

print("Parser test passed!")
print(jobs[0])