import sys
import tty
import termios

def getKey():
    """Reads a single key press and blocks until a key is pressed."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)  # Set terminal to raw mode (no buffering)
        key = sys.stdin.read(1)  # Read a single character
        
        if key == '\x1b':
            key += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings

    return key

def hideCursor(func):
    """Decorator that hides the cursor before running the function and shows it afterwards."""
    def wrapper(*args, **kwargs):
        try:
            print("[?25l", end='')  # Hide cursor
            return func(*args, **kwargs)
        finally:
            print("[?25h", end='')  # Show cursor
    return wrapper

def removeLines(n: int):
    """Removes the last n lines from the terminal."""
    for _ in range(n):
        print("[F[K", end='')

__all__ = ['getKey', 'hideCursor', 'removeLines']