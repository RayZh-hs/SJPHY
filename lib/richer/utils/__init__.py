from .console import (
    getKey,
    hideCursor,
    removeLines,
)

KEY_CODE = {
    'up': '\x1b[A', "down": '\x1b[B', "right": '\x1b[C', "left": '\x1b[D', "enter": '\r', "space": ' ', "ctrl_c": '\x03'
}

__all__ = [
    'getKey',
    'hideCursor',
    'removeLines',
    'KEY_CODE',
]