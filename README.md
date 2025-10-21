# SJPHY

End-to-end calculator for Physics Experiments in SJTU.

---

This project aims at providing fast, reliable physics experiment data analysis results including graphics and uncertainty analysis.

It is currently under active development. See the `dev` branch for up-to-date info.

## Installation

Ensure that you have Python and Git installed. First clone the repository:

```bash
git clone https://github.com/RayZh-hs/SJPHY.git
cd SJPHY
```

Since the project uses `uv` for environment management, install it if it is not already installed:

For linux and macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then within the folder, create and activate the environment:

```bash
uv sync
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

This should automatically setup and install all dependencies.

## Using Experiment Templates

Finish the installation steps above, then go to the `experiments` folder. Find the corresponding experiment folder. You can find a list in `experiments/experiments.md`.

In each folder, you will find a `main.ipynb` file. Open it with any code editor.

To use the template, copy the first python cell to a **reliable AI agent** (e.g. Google Gemini 2.5 Pro), along with **all photos of your worksheet**, constituting the all data needed to conduct analysis.
The AI agent should produce a python snippet extracting all data from the photos, formatting them into python lists or arrays.
**Replace the first cell with the produced code.**

Then, run all cells in order. The notebook should produce all analysis results, including uncertainty analysis and graphs.

You will see an `output` folder created in the experiment folder, containing:
- All generated graphs in PNG format;
- A markdown report including all analysis results, graphs, and uncertainty analysis.
- A pdf version of the report, rendered from the markdown file.
