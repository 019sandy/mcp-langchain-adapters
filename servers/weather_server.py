import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather") 
# It will return static string and is a dummy one

@mcp.tool()
async def get_weather(Location: str) -> str:
    """Get the weather for a given location"""
    return f"The weather in {Location} is sunny as always"


if __name__ == "__main__":
  mcp.run(transport="sse") # here we are using sse for now