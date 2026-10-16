from mcp import Client

HIRINGCAFE_URL = "https://hiringcafe.com/api/mcp"


async def get_job_details(job_id: str) -> str:
    '''Fetch the full details of a HiringCafe job using its ID.'''

    async with Client(HIRINGCAFE_URL) as client:
        result = await client.call_tool(
            "get_job_details",
            {"job_id": job_id}
        )


    if result.is_error:
        error_text = "\n".join(
            block.text
            for block in result.content
            if hasattr(block, "text")
        )
        raise RuntimeError(f"Failed to fetch job details: \n{error_text}")

    return "\n".join(
        block.text
        for block in result.content
        if hasattr(block, "text")
    )