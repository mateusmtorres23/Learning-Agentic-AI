from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search

search_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='search_agent',
    description='A specialized web search assistant.',
    instruction="""
    You are a specialized web search assistant. 
    When the coding agent asks you to find an answer, use the google_search tool to find the answer.
    """,
    tools=[google_search]
)

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='root_agent',
    description='You are the main agent and the orchestrator. Also a specialized coding assistant. Use the search agent to find answers to user questions when you do not know the answer.',
    instruction="""
    You are a specialized coding assistant. 
    Answer user questions to the best of your knowledge. 
    If you do not know the answer, ask the search agent to find the answer.
    """,
    tools=[AgentTool(agent=search_agent)]
)
