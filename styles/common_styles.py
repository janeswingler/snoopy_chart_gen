import random
import matplotlib.pyplot as plt

# Shared constants
FONT_NAMES = [
    'Arial', 'Calibri', 'Times New Roman', 'Courier New', 'Verdana', 'Georgia',
    'Comic Sans MS', 'Impact', 'Tahoma', 'Trebuchet MS', 'Garamond'
]
FONT_SIZES = [14, 16, 20, 22, 24, 26]
FONT_WEIGHTS = ['normal', 'bold']
FONT_COLORS = ['black', 'gray', 'red', 'blue', 'green', 'purple']
SEABORN_PALETTES = [
    'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'tab10', 'tab20',
    'Set1', 'Set2', 'Set3', 'Paired', 'Accent', 'Blues', 'BuGn', 'BuPu', 'GnBu',
    'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples',
    'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'
]
EDGE_COLORS = ['black', 'gray', 'none', 'white']
LINE_WIDTHS = [1, 1.5, 2]

# Utility functions
def apply_random_font_style():
    """
    Apply random font style to current plot.
    """
    font_style = {
        'fontname': random.choice(FONT_NAMES),
        'fontsize': random.choice(FONT_SIZES),
        'weight': random.choice(FONT_WEIGHTS),
        'color': random.choice(FONT_COLORS)
    }
    plt.title(plt.gca().get_title(), **font_style)
    plt.xlabel(plt.gca().get_xlabel(), **font_style)
    plt.ylabel(plt.gca().get_ylabel(), **font_style)

    ax = plt.gca()
    for tick in ax.get_xticklabels():
        tick.set_fontname(font_style['fontname'])
        tick.set_fontsize(font_style['fontsize'])
        tick.set_weight(font_style['weight'])
        tick.set_color(font_style['color'])
    for tick in ax.get_yticklabels():
        tick.set_fontname(font_style['fontname'])
        tick.set_fontsize(font_style['fontsize'])
        tick.set_weight(font_style['weight'])
        tick.set_color(font_style['color'])

    plt.gcf().autofmt_xdate()

def apply_random_background():
    """
    Apply random background style to current plot.
    """
    background_colors = ['lightyellow', 'lightblue', 'lightgreen', 'lavender', 'aliceblue', 'honeydew']
    grid_styles = ['--', '-.', ':', 'solid']
    grid_widths = [0.5, 1, 1.5]
    block_styles = ['solid', 'dotted', 'dashed']

    background_color = random.choice(background_colors)
    plt.gca().set_facecolor(background_color)

    if random.choice([True, False]):
        grid_style = random.choice(grid_styles)
        grid_width = random.choice(grid_widths)
        plt.grid(visible=True, linestyle=grid_style, linewidth=grid_width, color='gray', alpha=0.7)
    if random.choice([True, False]):
        plt.gca().patch.set_edgecolor('black')
        plt.gca().patch.set_linewidth(random.choice(grid_widths))
        plt.gca().patch.set_linestyle(random.choice(block_styles))
        plt.gca().patch.set_alpha(0.2)

def apply_random_tick_style():
    """
    Apply random tick style to current plot.
    """
    tick_lengths = [4, 6, 8, 10]
    tick_widths = [0.5, 1, 1.5]
    tick_directions = ['in', 'out', 'inout']

    ax = plt.gca()
    tick_length = random.choice(tick_lengths)
    tick_width = random.choice(tick_widths)
    tick_direction = random.choice(tick_directions)

    ax.tick_params(axis='both', which='major', length=tick_length, width=tick_width, direction=tick_direction)
    ax.tick_params(axis='both', which='minor', length=tick_length / 2, width=tick_width / 2, direction=tick_direction)