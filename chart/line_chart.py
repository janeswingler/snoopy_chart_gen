import matplotlib.pyplot as plt
import random
from styles.line_styles import apply_line_style
from data_generator import DataGenerator
from chart.chart import Chart

class LineChart(Chart):
    """
    Class for generating and plotting line chart with optional misleading features.
    """
    line_count = 0  # Class variable to keep track of line chart count for the id's

    def __init__(self, title='', misleading_feature=None, x_label='', y_label='', source=''):
        """
        Initialize line chart with title, misleading feature, axis labels, and source.
        """
        super().__init__(title)
        self.misleading_feature = misleading_feature
        self.x_label = x_label
        self.y_label = y_label
        self.source = source
        LineChart.line_count += 1
        self.chart_id = f"line{LineChart.line_count}"
        self.category_type = None

    def generate_data(self):
        """
        Generate line chart data based on the misleading feature.
        """
        data_gen = DataGenerator()
        if self.misleading_feature == "Inconsistent Time Intervals":
            self.x_values, self.y_values, self.category_type = data_gen.generate_inconsistent_time_series()
        else:
            self.x_values, self.y_values, self.category_type = data_gen.generate_time_series()

        self.data = {'x_values': self.x_values, 'y_values': self.y_values}

    def plot(self):
        """
        Plot the line chart and apply misleading feature if specified.
        """
        fig_width = random.uniform(12, 15)
        fig_height = random.uniform(8, 10)
        plt.figure(figsize=(fig_width, fig_height))

        line, = plt.plot(self.x_values, self.y_values, marker='o')
        plt.title(self.title)
        plt.xlabel(self.x_label if self.x_label else (self.category_type if self.category_type else 'Categories'))
        plt.ylabel(self.y_label if self.y_label else 'Values')

        apply_line_style(line)

    def get_specific_json_data(self):
        """
        Get subclass-specific JSON data for line chart.
        """
        return {
            'x_label': self.x_label if self.x_label else (self.category_type if self.category_type else 'Time'),
            'y_label': self.y_label,
            'source': self.source
        }

    def get_chart_type(self):
        """
        Return the chart type as 'line'.
        """
        return 'line'