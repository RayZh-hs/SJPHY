from rich.prompt import Prompt
from rich.console import Console
from richer.utils import removeLines
from typing import Optional, Callable

def input(prompt: str, validator: Optional[Callable[[str], bool]] = None, empty_ok: bool = False) -> str:
    """Get user input with a prompt."""
    console = Console()
    line_count = 1
    while True:
        user_input = Prompt.ask(prompt)
        if not user_input and not empty_ok:
            removeLines(1)
            continue
        if validator and not validator(user_input):
            removeLines(line_count)
            console.print("[red]Invalid input. Please try again.[/red]")
            continue
        if line_count == 1:
            line_count += 1
        return user_input