import asyncio
from mcp import Client

HIRINGCAFE_URL = "https://hiringcafe.com/api/mcp"

async def main():
    async with Client(HIRINGCAFE_URL) as client:
        result = await client.list_tools()

        for tool in result.tools:
            print(f"\nTool: {tool.name}")
            print(f"Description: {tool.description}")
            print(f"Input Schema: {tool.input_schema}")


if __name__=="__main__":
    asyncio.run(main())