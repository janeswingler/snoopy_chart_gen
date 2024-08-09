import random
import seaborn as sns
from styles.common_styles import apply_random_font_style, SEABORN_PALETTES, EDGE_COLORS, LINE_WIDTHS, FONT_NAMES, FONT_SIZES, FONT_WEIGHTS, FONT_COLORS

def apply_pie_style(elements, texts, autotexts):
    """
    Apply random style to pie chart.
    """
    palette_name = random.choice(SEABORN_PALETTES)
    palette = sns.color_palette(palette_name, len(elements))
    edge_color = random.choice(EDGE_COLORS)
    line_width = random.choice(LINE_WIDTHS)
    for wedge, color in zip(elements, palette):
        wedge.set_edgecolor(edge_color)
        wedge.set_linewidth(line_width)
        wedge.set_facecolor(color)

    font_name = random.choice(FONT_NAMES)
    font_size = random.choice(FONT_SIZES)
    font_weight = random.choice(FONT_WEIGHTS)
    font_color = random.choice(FONT_COLORS)

    for text in texts:
        text.set_fontname(font_name)
        text.set_fontsize(font_size)
        text.set_weight(font_weight)
        text.set_color(font_color)

    for autotext in autotexts:
        autotext.set_fontname(font_name)
        autotext.set_fontsize(font_size)
        autotext.set_weight(font_weight)
        autotext.set_color(font_color)

    apply_random_font_style()