import yaml
from rich import print
from rich.prompt import Prompt
from pathlib import Path
from typing import TypedDict

class Student(TypedDict):
    student_name: str
    student_id: int

def _port_me_dot_yaml() -> Student:
    """Get the path to the me.yaml configuration file."""
    import os

    # /lib/me/__init__.py
    project_root = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
    me_yaml_path = project_root / "me.yaml"
    
    if not me_yaml_path.exists():
        print(f"[yellow]在 {me_yaml_path} 未找到配置文件 me.yaml, 创建中[/yellow]")
        student_name = Prompt.ask("Enter your name 请输入你的姓名")
        student_id = Prompt.ask("Enter your student ID 请输入你的学号")
        
        with open(me_yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump({
                'student_name': student_name,
                'student_id': student_id
            }, f, allow_unicode=True)
        print(f"[green]✅ me.yaml 已经在 {me_yaml_path} 被创建，你可以随时修改其中的值。[/green]")
        print("[green]✅ 这会影响你渲染的图标上的个人信息。[/green]")
    
    with open(me_yaml_path, 'r', encoding='utf-8') as f:
        string = f.read()
        # Validate against YAML format
        try:
            dic = yaml.safe_load(string)
            return Student(**dic)
        except yaml.YAMLError as e:
            print(f"[red]❌ 解析 me.yaml 时出错: {e}[/red]")
            raise

def get() -> Student:
    """Get the student information from me.yaml."""
    return _port_me_dot_yaml()

def get_name() -> str:
    """Get the student name from me.yaml."""
    return get()['student_name']

def get_id() -> int:
    """Get the student ID from me.yaml."""
    return get()['student_id']

__all__ = [
    "get",
    "get_name",
    "get_id",
]