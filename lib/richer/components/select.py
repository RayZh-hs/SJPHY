from rich.console import Console
from rich.text import Text
from richer.utils import getKey, hideCursor, removeLines, KEY_CODE
from typing import List


def select(
    prompt: str,
    options: List[str],
    default_index: int = 0,
    show_cursor: bool = True
) -> int:
    """
    Display a keyboard-driven selector for the user to choose from a list of options.
    
    Args:
        prompt: The prompt message to display
        options: List of options to choose from
        default_index: Default selected option index (0-based)
        allow_empty: If True, allows user to exit without selecting (returns None)
        show_cursor: If True, shows a cursor indicator next to the selected option
        
    Returns:
        The selected option string, or None if allow_empty is True and user cancels
    """ 
    console = Console()
    selected_index = max(0, min(default_index, len(options) - 1))
    
    @hideCursor
    def _display_selector() -> int:
        nonlocal selected_index
        
        # Create the display content
        content = Text()
        content.append(prompt + "\n\n")
        
        # Display each option
        for i, option in enumerate(options):
            if i == selected_index:
                # Highlight selected option
                if show_cursor:
                    content.append("> ", style="bold yellow")
                content.append(option, style="bold yellow")
            else:
                # Regular option
                if show_cursor:
                    content.append("  ")
                content.append(option)
            
            if i < len(options) - 1:
                content.append("\n")
        
        # Display instructions
        content.append("\n\nUse ↑/↓ to navigate, Enter to select", style="dim")
        
        console.print(content)
        
        # Get user input
        while True:
            key = getKey()
            
            if key == KEY_CODE['up']:
                selected_index = (selected_index - 1) % len(options)
                # Clear the previous display and redraw
                removeLines(len(options) + 4)
                return _display_selector()
                
            elif key == KEY_CODE['down']:
                selected_index = (selected_index + 1) % len(options)
                # Clear the previous display and redraw
                removeLines(len(options) + 4)
                return _display_selector()
                
            elif key == KEY_CODE['enter']:
                # Clear the selector display
                removeLines(len(options) + 4)
                return selected_index
                
            elif key == KEY_CODE['ctrl_c']:
                exit(0)
    
    ret = _display_selector()
    # Remove all the lines and print the selected option\
    console.print(prompt, end=" ")
    console.print(options[ret], style="bold yellow", highlight=False)
    return ret
