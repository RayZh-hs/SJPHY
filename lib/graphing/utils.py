import numpy as np
from scipy.stats import linregress

def plot_graph(ax, x_data, y_data, options) -> dict:
    """
    A utility function to create a styled subplot with extensive options.

    Args:
        ax (matplotlib.axes.Axes): The subplot axes to draw on.
        x_data (array-like): The x-axis data.
        y_data (array-like): The y-axis data.
        options (dict): A dictionary containing configuration for the plot.
            - "title" (str): Plot title.
            - "xlabel" (str): X-axis label.
            - "ylabel" (str): Y-axis label.
            - "xlim" (tuple): X-axis limits.
            - "ylim" (tuple): Y-axis limits.
            - "color" (str): Primary color for the plot.
            - "exclude_points" (list): Indices of points to exclude from the main line/fit.
            - "linear_regression" (bool): If True, perform and plot a linear regression.
            - "regression_range" (float): Fraction of x-axis range to use for regression line extension.
            - "regression_label_font_size" (int): Font size for regression equation label.
            - "regression_box_location" (str): Position for the regression info box.
                Options: 'upper left', 'upper right', 'lower left', 'lower right',
                         'upper center', 'lower center', 'center left', 'center right', 'center'.
            - "info_box" (dict): Optional box for metadata.
                Example: {
                    'location': 'lower right',
                    (optional) 'offset': (0.0, 0.0),
                    'data': {
                        'Name': 'Your Name',
                        'Student ID': '12345',
                        'Date': '2025-10-22'
                    }
                }
    """
    
    ret = dict()
    
    # --- Data Preparation ---
    exclude_indices = options.get("exclude_points", [])
    color = options.get("color", "black")

    x_included = [x for i, x in enumerate(x_data) if i not in exclude_indices]
    y_included = [y for i, y in enumerate(y_data) if i not in exclude_indices]
    x_excluded = [x_data[i] for i in exclude_indices]
    y_excluded = [y_data[i] for i in exclude_indices]

    # --- Plotting Data Points ---
    # If doing a linear fit, just plot markers. Otherwise, connect with a line.
    linestyle = 'None' if options.get("linear_regression") else '-'
    ax.plot(x_included, y_included, color=color, marker='o', linestyle=linestyle)
    if x_excluded:
        ax.scatter(x_excluded, y_excluded, s=120, facecolors='none', edgecolors=color)

    # --- Position Mapping for Text Boxes ---
    # Maps user-friendly strings to (x, y, horizontal_align, vertical_align) tuples
    position_map = {
        'upper left':   (0.05, 0.95, 'left', 'top'),
        'upper right':  (0.95, 0.95, 'right', 'top'),
        'lower left':   (0.05, 0.05, 'left', 'bottom'),
        'lower right':  (0.95, 0.05, 'right', 'bottom'),
        'upper center': (0.50, 0.95, 'center', 'top'),
        'lower center': (0.50, 0.05, 'center', 'bottom'),
        'center left':  (0.05, 0.50, 'left', 'center'),
        'center right': (0.95, 0.50, 'right', 'center'),
        'center':       (0.50, 0.50, 'center', 'center'),
    }

    # --- Linear Regression Box ---
    if options.get("linear_regression", False):
        lin_fit = linregress(x_included, y_included)
        slope, intercept, r_value = lin_fit.slope, lin_fit.intercept, lin_fit.rvalue    # type: ignore
        r_squared = r_value**2
        ret['k'] = slope
        ret['b'] = intercept
        ret['r_squared'] = r_squared

        # Create the line of best fit across the entire x-axis range
        x_lim = options.get("xlim")
        regression_range = options.get("regression_range", 0.9)
        regression_leave = (1 - regression_range) / 2
        x_from = x_lim[0] * regression_leave + x_lim[1] * (1 - regression_leave)
        x_to = x_lim[0] * (1 - regression_leave) + x_lim[1] * regression_leave
        fit_x = np.linspace(x_from, x_to, 100)
        fit_y = slope * fit_x + intercept
        ax.plot(fit_x, fit_y, color=color, linestyle='-', label='Linear Fit')

        # Format text for the box
        op = '+' if intercept >= 0 else ''
        equation = f'$y = {slope:.4f}x {op} {intercept:.4f}$'
        r_squared_text = f'$R^2 = {r_squared:.4f}$'
        full_text = f'{equation}\n{r_squared_text}'

        # Get position from options, defaulting to 'upper left'
        location_key = options.get("regression_box_location", "upper left")
        pos_params = position_map.get(location_key, position_map['upper left'])

        ax.text(pos_params[0], pos_params[1], full_text,
                transform=ax.transAxes, fontsize=16,
                ha=pos_params[2], va=pos_params[3],
                bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.6))

    # --- Optional Info Box ---
    info_box_config = options.get("info_box")
    if info_box_config and isinstance(info_box_config, dict):
        data = info_box_config.get("data", {})
        offset = info_box_config.get("offset", (0.0, 0.0))
        if data:
            # Format the dictionary data into a multi-line string
            info_text = '\n'.join([f'{key}: {value}' for key, value in data.items()])

            # Get position from the config, defaulting to 'lower right'
            location_key = info_box_config.get("location", "lower right")
            pos_params = position_map.get(location_key, position_map['lower right'])

            ax.text(pos_params[0] + offset[0], pos_params[1] + offset[1], info_text,
                    transform=ax.transAxes, fontsize=14,
                    ha=pos_params[2], va=pos_params[3],
                    bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.6))

    ax.set_title(options.get("title", ""))
    ax.set_xlabel(options.get("xlabel", ""))
    ax.set_ylabel(options.get("ylabel", ""))
    ax.set_xlim(*options.get("xlim", (None, None)))
    ax.set_ylim(*options.get("ylim", (None, None)))
    ax.grid(True)
    
    return ret