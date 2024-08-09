import random
import seaborn as sns
from styles.common_styles import apply_random_font_style, SEABORN_PALETTES, EDGE_COLORS, LINE_WIDTHS

BAR_WIDTHS = [0.4, 0.6, 0.8,]
EDGE_STYLES = ['solid', 'dotted', 'dashed']
HATCH_PATTERNS = ['', '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

def apply_bar_style(bars):
    """
    Apply random style to bar chart.
    """
    palette_name = random.choice(SEABORN_PALETTES)
    palette = sns.color_palette(palette_name, len(bars))
    bar_width = random.choice(BAR_WIDTHS)
    edge_color = random.choice(EDGE_COLORS)
    line_width = random.choice(LINE_WIDTHS)
    edge_style = random.choice(EDGE_STYLES)
    use_hatch = random.choice([True, False])

    for bar, color in zip(bars, palette):
        bar.set_facecolor(color)
        if use_hatch:
            bar.set_hatch(random.choice(HATCH_PATTERNS))
        if edge_style:
            bar.set_edgecolor(edge_color)
            bar.set_linewidth(line_width)
            bar.set_linestyle(edge_style)
        else:
            bar.set_edgecolor(color)
            bar.set_linewidth(0)
        bar.set_width(bar_width)

    apply_random_font_style()