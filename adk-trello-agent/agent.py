from google.adk.agents.llm_agent import Agent
from datetime import datetime
from trello_services import add_task, list_tasks, change_task_status, remove_task

def get_temporal_context() -> str:
    now = datetime.now()
    temporal_context = f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    return temporal_context

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A Task manager agent that helps organize and manage tasks effectively.',
    instruction="""
                You are a Task manager agent that helps organize and manage tasks effectively. 
                You will receive projects or tasks from the user and break them down to organize them.
                Your goal is to help the user stay organized and ensure that all tasks are correctly managed.
                Help the user bringing temporal context to the table.
                Your functions:
                1. Add new tasks to the Trello board
                2. List all tasks in the Trello board and their status (To do, In progress, Done)
                3. Update the status of a task (move it to the correct list in Trello)
                4. Remove tasks from the Trello board when they are completed or no longer needed
                5. Generate temporal context to help manage deadlines and prioritize tasks effectively
                Output: Always respond in a structured format.
                """,
    tools=[add_task, get_temporal_context, list_tasks, change_task_status, remove_task]
)
