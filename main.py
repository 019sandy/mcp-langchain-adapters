import asyncio
from dotenv import load_dotenv
import os 

# Importing MCP Objects
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


# Importing Lancghain Adapters
from langchain_mcp_adapters.tools import load_mcp_tools

# For Orchestation
from langgraph.prebuilt import create_react_agent


load_dotenv() 
#1.
llm = ChatOpenAI(model_name="gpt-4o-mini")

#2.
stdio_server_params = StdioServerParameters(
    command="C:/Users/SandeepGupta1/miniconda3/python.exe",
    args=["C:/mcp-langchain/servers/math_server.py"],
    
)

async def main():
   #3.
   async with stdio_client(stdio_server_params) as (read,write):
        #4.
        async with ClientSession(read_stream=read, write_stream=write) as session:
            #5.1
            await session.initialize()
            print("Session initialized")
            #5.2
            # tools = await session.list_tools() -> Replace it with Langhcian Object
            tools = await load_mcp_tools(session)
            print(tools)

            #5.3
            agent = create_react_agent(llm,tools)

            #5.4
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 2+ 2")]})
            print(result["messages"][-1].content)

            

if __name__ == "__main__":
    asyncio.run(main())
    
