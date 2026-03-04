<div align="center">
    <img src="resources/logo/logo.png" width="180" alt="SJPHY Logo"/>
    <h2>SJPHY</h2>
    <span>上海交通大学物理实验分析器</span>
</div>

---

[English](README.md) | **中文**

本项目旨在为物理实验数据分析提供快速、可靠的结果，包括图表绘制和不确定度分析。

项目目前正在积极开发中。请查看 `dev` 分支获取最新信息。

## 安装

确保已安装 Python 和 Git。首先克隆仓库：

```bash
git clone https://github.com/RayZh-hs/SJPHY.git
cd SJPHY
```

本项目使用 `uv` 进行环境管理，如尚未安装，请先安装：

Linux 和 macOS：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows（PowerShell）：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

然后在项目文件夹中，创建并激活环境：

```bash
uv run poe sync             # 创建环境、安装依赖并链接 sjphy 动态 Python 库
```

激活环境。macOS/Linux：

```bash
source .venv/bin/activate
```

Windows：

```powershell
.venv\Scripts\activate
```

以上步骤将自动设置并安装所有依赖项。

## 使用实验模板

完成上述安装步骤后，进入 `experiments` 文件夹，找到对应的实验文件夹。实验列表可在 `experiments/experiments.md` 中查看。

每个文件夹中都有一个 `main.ipynb` 文件，使用任意代码编辑器打开即可。

使用模板时，将第一个 Python 单元格的内容复制给一个**可靠的 AI 大语言模型**（如 Google Gemini 2.5 Pro），同时附上**你实验报告上所有实验数据表的照片**。AI 会生成一个从照片中提取所有数据的 Python 代码片段。将第一个单元格的内容替换为该片段，然后逐个运行文件的单元格。部分 Notebook 需要你填写或调整一些参数，如果输出不符合预期，请留意其中的注释说明。

然后按顺序运行所有单元格。Notebook 将自动生成所有分析结果，包括不确定度分析和图表。如果这是你第一次运行任何 Notebook，系统可能要求你填写姓名和学号以生成报告。该信息将保存在项目根目录的 `me.yaml` 文件中，如果有误你可以手动修改该文件。

实验文件夹中会生成一个 `output` 文件夹，包含：
- 所有生成的 PNG 格式图表；

运行单元格时，所有所需数据将按顺序打印输出。

## 致谢

项目 Logo 来自 [FlatIcon](https://www.flaticon.com/)，由 smalllikeart 设计。
