import yaml
from rich import print
from pathlib import Path
from typing import TypedDict

class Student(TypedDict):
    student_name: str
    student_id: int

def _get_me_path() -> Path:
    """Get the path to the me.yaml configuration file."""
    import os

    # /lib/me/__init__.py
    project_root = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
    me_yaml_path = project_root / "me.yaml"
    
    return me_yaml_path

def exists() -> bool:
    """Check if the me.yaml configuration file exists."""
    me_yaml_path = _get_me_path()
    return me_yaml_path.exists()

def set(student_name: str, student_id: int) -> None:
    """Create or overwrite the me.yaml configuration file."""
    me_yaml_path = _get_me_path()
    data = {
        "student_name": student_name,
        "student_id": student_id
    }
    with open(me_yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
    print(f"[green]✅ me.yaml created/updated at {me_yaml_path}[/green]")

def get() -> Student:
    """Get the student information from me.yaml."""
    if not exists():
        raise FileNotFoundError("me.yaml does not exist. Please create it using set_me_yaml().")
    me_yaml_path = _get_me_path()
    with open(me_yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return Student(student_name=data['student_name'], student_id=data['student_id'])

def get_name() -> str:
    """Get the student name from me.yaml."""
    return get()['student_name']

def get_id() -> int:
    """Get the student ID from me.yaml."""
    return get()['student_id']

__all__ = [
    "exists",
    "set",
    "get",
    "get_name",
    "get_id",
]