from matplotlib import rcParams
from cycler import cycler
from .font import SONGTI_FONT_FAMILY

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = [SONGTI_FONT_FAMILY, 'SimSun', 'Source Han Serif', 'Times New Roman']
rcParams['font.size'] = 15
rcParams['axes.linewidth'] = 1.1
rcParams['axes.labelpad'] = 5.0
plot_color_cycle = cycler('color', ['#000000', '#0000FE', '#FE0000', '#008001', '#FD8000', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
rcParams['axes.prop_cycle'] = plot_color_cycle
rcParams['axes.xmargin'] = 0
rcParams['axes.ymargin'] = 0