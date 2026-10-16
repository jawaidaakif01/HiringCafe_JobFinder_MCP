from mcp import Client
from job_parser import parse_jobs


HIRINGCAFE_URL = "https://hiringcafe.com/api/mcp"

async def search_jobs(
    query: str,
    location: str = "",
    employment_type: str = "Any",
    limit: int = 10
) -> list[dict]:
    '''Search HiringCafe and return parsed job listings.'''

    # Build the arguments accepted by HiringCafe's search_job tool.
    arguments = {
        "search": query,
        "limit": 25
    }

    if location.strip():
        arguments["location"] = location.strip()

    if employment_type != "Any":
        arguments["employment_types"] = [employment_type]


    async with Client(HIRINGCAFE_URL) as client:
        result = await client.call_tool(
            "search_jobs",
            arguments
        )

    if result.is_error:
        error_text = "\n".join(
            block.text
            for block in result.content
            if hasattr(block, "text")
        )

        raise RuntimeError(f"HiringCafe search failed:\n{error_text}")

    # Collect the text returned by the MCP tool.
    markdown = "\n".join(
        block.text
        for block in result.content
        if hasattr(block, "text")
    )

    # Convert Markdown into Python Dictionaries.
    jobs = parse_jobs(markdown)

    for job in jobs:
        print(
            f"Title: {job.get('title')} |"
            f"Employment: {job.get('employment_type')!r}"
        )

    # Validate employment type locally as well.
    if employment_type != "Any":
        requested_type = employment_type.strip().casefold()

        jobs = [
            job for job in jobs if requested_type in {
                item.strip().casefold() for item in (job.get("employment_type") or "").split(",")
            }
        ]


    return jobs[:limit]


    