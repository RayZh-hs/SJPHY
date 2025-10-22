from matplotlib import font_manager as fm
from pathlib import Path
import rich

font_path = Path(__file__).parent.parent.parent / "resources" / "fonts" / "songti-sc-regular.ttf"

if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    SONGTI_FONT_FAMILY = fm.FontProperties(fname=str(font_path)).get_name()
    rich.print(f"[green]✔ Registered font:[/green] {SONGTI_FONT_FAMILY}")
else:
    SONGTI_FONT_FAMILY = "Serif"
    rich.print(f"[red]✖ Font file not found. Using fallback font:[/red] {SONGTI_FONT_FAMILY}")

__all__ = ["SONGTI_FONT_FAMILY"]