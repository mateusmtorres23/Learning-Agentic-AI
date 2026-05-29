from google.adk.agents.llm_agent import Agent
from google.adk.tools.toolbox_toolset import ToolboxToolset

toolset = ToolboxToolset(
    server_url="http://127.0.0.1:5000"
)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='postgres_agent',
    description="""You the agent from a bank and you exist to help bankers 
                   to acess transactions info per demand""",
    instruction='Answer user questions to the best of your knowledge',
    tools=[toolset]
)

