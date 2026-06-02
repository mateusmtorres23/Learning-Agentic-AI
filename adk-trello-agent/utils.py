from trello import TrelloClient, Card, Board
from dotenv import load_dotenv
from typing import Optional
import os

load_dotenv()

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_SECRET = os.getenv('TRELLO_API_SECRET')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')

trello_client = TrelloClient(
    api_key=TRELLO_API_KEY,
    api_secret=TRELLO_API_SECRET,
    token=TRELLO_API_TOKEN
)

def trello_task_board() -> Board:
    boards = trello_client.list_boards()
    return [b for b in boards if b.name == 'Python automated board'][0]

def find_task_card(task_name: str) -> Optional[Card]:
    task_board = trello_task_board()
    lists = task_board.list_lists()

    task_card = None
    for l in lists:
        cards = l.list_cards()
        card = next(
            (c for c in cards if c.name == task_name),
            None
        )
        task_card = card if card else None

    return task_card