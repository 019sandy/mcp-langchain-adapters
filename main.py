import asyncio
from dotenv import load_dotenv
import os 

# Importing MCP Objects
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI

# Importing Lancghain Adapters
from langchain_mcp_adapters.tools import load_mcp_tools

# For Orchestation
from langgraph.prebuilt import create_react_agent


load_dotenv() 
#1.
llm = ChatOpenAI(model_name="gpt-4o-mini")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/mcp-langchainservers/math_server.py"],
    
)

async def main():
    print("Hello from mcp-langchain!")


if __name__ == "__main__":
    asyncio.run(main())
