from .utils import trello_task_board, find_task_card

def add_task(task_name: str, task_description: str, due_date: str):
    task_board = trello_task_board()
    todo_list = [l for l in task_board.list_lists() if l.name == 'To do'][0]

    todo_list.add_card(name=task_name, desc=task_description, due=due_date)

def list_tasks():
    task_board = trello_task_board()

    tasks = []
    for lst in task_board.list_lists():
        for card in lst.list_cards():
            tasks.append((card.name, card.desc, card.due, lst.name))

    return tasks

def change_task_status(task_name:str, new_status:str) -> str:
    try:
        task_board = trello_task_board()
        lists = task_board.list_lists()

        status_map = {
            'to do' : 'To do',
            'in progress' : 'In progress',
            'done' : 'Done'
        }

        new_status_name = status_map.get(new_status.lower())

        if not new_status_name:
            return 'Invalid status: use "to do", "in progress" or "done"'
        
        new_task_list = next(
            (l for l in lists if l.name.upper() == new_status_name.upper()),
            None
        )

        if not new_task_list:
            return f'The list {new_status} was not found'
        
        task_card = find_task_card(task_name)

        if not task_card:
            return f"The task {task_name} was not found try listing the tasks to find the correct one"

        task_card.change_list(new_task_list.id)
        return f'Task {task_name} is now {new_task_list.name}'
    
    except Exception as e:
        return f'error: {e}'
    
def remove_task(task_name: str):
    task_card = find_task_card(task_name)

    if not task_card:
        return f'The task {task_name} was not found try listing the tasks to find the correct one'

    task_card.delete()