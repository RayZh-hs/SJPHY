from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.table import Table
from rich_gradient.text import Text as GradientText

__title_art__ = r"""
 ███████╗     ██╗██████╗ ██╗  ██╗██╗   ██╗
 ██╔════╝     ██║██╔══██╗██║  ██║╚██╗ ██╔╝
 ███████╗     ██║██████╔╝███████║ ╚████╔╝ 
 ╚════██║██   ██║██╔═══╝ ██╔══██║  ╚██╔╝  
 ███████║╚█████╔╝██║     ██║  ██║   ██║   
 ╚══════╝ ╚════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   

End-to-end physics experiment calculator
"""


def help():
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
        "🔬 [bold green]Automated[/bold green] physics experiment analysis",
        "📓 [bold green]Jupyter[/bold green] notebook based workflow",
        "📈 [bold green]Rich[/bold green] visualizations and reports",
        "⚙️ [bold green] Configurable[/bold green] analysis parameters"
    ]
    
    features_text = Text("\n").join(Text.from_markup(f) for f in features)
    features_panel = Panel(
        features_text,
        title="[bold magenta]✨ Features[/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    # Create a table to hold both panels side by side
    table = Table(show_header=False, box=None, padding=0, expand=True)
    table.add_column(width=60, ratio=1)  # Left column for description panel
    table.add_column(width=50, ratio=1)  # Right column for features panel
    table.add_row(desc_panel, features_panel)
    
    # Print the table with both panels
    console.print(table)
    console.print("")


if __name__ == "__main__":
    help()
