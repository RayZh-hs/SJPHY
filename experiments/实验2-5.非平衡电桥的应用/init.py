from rich.console import Console
from rich.text import Text
from rich.rule import Rule
from richer.components import panel_select
from richer.utils import readUntilEOF

from os.path import dirname, join, exists
from pyperclip import copy
import json

def get_prompt() -> str:
    with open(join(dirname(__file__), 'main.ipynb'), 'r', encoding='utf-8') as f:
        raw = f.read()
    notebook = json.loads(raw)
    return ''.join(notebook['cells'][1]['source'])

def init():
    console = Console()
    if exists(join(dirname(__file__), 'data.yaml')):
        query = panel_select(
            prompt=Text("⚠️  data.yaml 已经存在，是否覆写已有数据？"),
            options=["y", "n"],
            default_index=0,
            max_width=60,
            color="yellow",
        )
        if query == 1:
            exit(0)
    with open(join(dirname(__file__), 'data.yaml'), 'w', encoding='utf-8') as f:
        f.write("")
    
    console.print("")
    console.print(Rule(title="[bold green]⚙️ 创建数据文件[/bold green]"))
    
    # Copy prompt to clipboard
    prompt = get_prompt()
    copy(prompt)
    
    console.print("")
    console.print("ℹ️  提示词已经拷贝到剪切板。请将其粘贴给拥有多模态能力的 AI 模型，并将自己的实验报告拍照上传。")
    console.print("ℹ️  请将输出的代码块中内容粘贴到下面，输入 ctrl+D (Linux/Mac) 或 ctrl+Z (Windows) 结束输入。")
    console.print("- Google Gemini: https://aistudio.google.com")
    console.print("- Deepseek: https://chat.deepseek.com/")
    console.print("")
    console.print("📋 粘贴代码块内容：")
    data = readUntilEOF()
    with open(join(dirname(__file__), 'data.yaml'), 'w', encoding='utf-8') as f:
        f.write(data)
    console.print("")
    console.print("[bold green]✅ 数据文件写入成功！[/bold green]")
    console.print("")
    console.print("🎉 请打开 main.ipynb 文件，运行全部内容。")

init()
