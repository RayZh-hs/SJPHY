from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.table import Table
from rich_gradient.text import Text as GradientText
from rich.rule import Rule
from richer.components import input

import me

__title_art__ = r"""
 ███████╗     ██╗██████╗ ██╗  ██╗██╗   ██╗
 ██╔════╝     ██║██╔══██╗██║  ██║╚██╗ ██╔╝
 ███████╗     ██║██████╔╝███████║ ╚████╔╝ 
 ╚════██║██   ██║██╔═══╝ ██╔══██║  ╚██╔╝  
 ███████║╚█████╔╝██║     ██║  ██║   ██║   
 ╚══════╝ ╚════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   

End-to-end physics experiment calculator
"""


def front_page():
    console = Console()
    
    # Display title with gradient effect using rich-gradient
    title_lines = __title_art__.split('\n')
    
    console.print("")
    for i, line in enumerate(title_lines):
        # Use rich-gradient Text to create a blue to red gradient
        gradient_line = GradientText(
            line,
            colors=["#fccb90", "#d57eeb"],
            rainbow=False,
            hues=10
        )
        console.print(Align.center(gradient_line))
    console.print("")
    
    # Create main description panel
    description = (
        "SJPHY is a suite of jupyter notebooks that aims to automatically analyze results "
        "from [bold blue]SJTU[/bold blue] physics experiments."
        "\n\n"
        "For more information, view the [bold yellow]README.md[/bold yellow] file"
    )
    
    desc_panel = Panel(
        Align.center(Text.from_markup(description, style="white")),
        title="[bold cyan]📊 About SJPHY[/bold cyan]",
        border_style="cyan",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    # Create features panel
    features = [
        "🔬 [bold green]AI-driven[/bold green] data extraction from worksheets",
        "💡 [bold green]Automated[/bold green] data analysis and graphing",
        "📈 [bold green]Rich[/bold green] visualizations and reports",
        "📓 [bold green]Jupyter[/bold green] notebook based workflow",
    ]
    
    features_text = Text("\n").join(Text.from_markup(f) for f in features)
    features_panel = Panel(
        features_text,
        title="[bold magenta]✨ Features[/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    # Use responsive layout based on console width
    mode = "parallel" if console.size.width >= 100 else "stacked"
    
    if mode == "parallel":
        # Pre-calculate heights to unify them
        options = console.options
        desc_width, feat_width = 60, 50
        desc_options = options.update(width=desc_width)
        desc_render = console.render_lines(desc_panel, desc_options, pad=False)
        feat_options = options.update(width=feat_width)
        feat_render = console.render_lines(features_panel, feat_options, pad=False)
        
        panel_height = max(len(desc_render), len(feat_render))
        desc_panel.height = panel_height - 1
        features_panel.height = panel_height - 1
        
        # Create a table to hold both panels side by side
        table = Table(show_header=False, box=None, padding=0, expand=True)
        table.add_column(width=desc_width, ratio=1)  # Left column for description panel
        table.add_column(width=feat_width, ratio=1)  # Right column for features panel
        table.add_row(desc_panel, features_panel)
        
        # Print the table with both panels
        console.print(table)
        console.print("")
    elif mode == "stacked":
        console.print(desc_panel)
        console.print("")
        console.print(features_panel)
        console.print("")

def init_me():
    if me.exists():
        return
    console = Console()
    console.print("🌟 It seems that this is the first time you are running [bold blue]SJPHY[/bold blue], welcome!")
    console.print("🌟 Let's set up your user profile.")
    console.print("🌟 All the information will be stored locally in the [bold yellow]me.yaml[/bold yellow] file.")
    console.print("")
    rule = Rule(title="[bold green]👤 User Profile Setup[/bold green]")
    console.print(rule)
    console.print("")
    console.print("[bold white]Tell me about yourself:[/bold white]")
    console.print("")
    name = input("👉 Your Name").strip()
    student_id = input("👉 Your Student ID", validator=(
        lambda x: x.isdigit() and len(x) == 12
    )).strip()
    me.set(name, int(student_id))
    console.print("")

def select_notebook():
    pass


if __name__ == "__main__":
    front_page()
    init_me()
    select_notebook()
