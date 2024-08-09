import random
import seaborn as sns
from styles.common_styles import apply_random_font_style, apply_random_background, apply_random_tick_style, SEABORN_PALETTES, LINE_WIDTHS, FONT_NAMES, FONT_SIZES, FONT_WEIGHTS, FONT_COLORS

MARKER_STYLES = ['o', 's', 'D', '^', 'v', '<', '>', 'p', 'P', '*', 'X']
MARKER_SIZES = [6, 8, 10, 12]

def apply_line_style(elements):
    """
    Apply random style to line chart.
    """
    palette_name = random.choice(SEABORN_PALETTES)
    palette = sns.color_palette(palette_name, 1)
    elements.set_linewidth(random.choice(LINE_WIDTHS))
    elements.set_color(palette[0])
    marker_style = random.choice(MARKER_STYLES)
    marker_size = random.choice(MARKER_SIZES)
    elements.set_marker(marker_style)
    elements.set_markersize(marker_size)
    elements.set_markerfacecolor(palette[0])
    elements.set_markeredgewidth(random.choice(LINE_WIDTHS) / 2)

    apply_random_background()
    apply_random_font_style()
    apply_random_tick_style()