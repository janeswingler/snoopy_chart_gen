import matplotlib.pyplot as plt
import random
from matplotlib.ticker import FuncFormatter
from styles.bar_styles import apply_bar_style
from data_generator import DataGenerator
from chart.chart import Chart

class BarChart(Chart):
    """
    Class for generating and plotting bar chart with optional misleading features.
    """
    bar_count = 0  # Class variable to keep track of bar chart count for ids

    def __init__(self, title='', misleading_feature=None):
        """
        Initialize bar chart with title and misleading feature.
        """
        super().__init__(title)
        self.misleading_feature = misleading_feature
        BarChart.bar_count += 1
        self.chart_id = f"bar{BarChart.bar_count}"
        self.y_start = 0
        self.category_type = ''
        self.x_label = ''
        self.source = ''
        self.y_label = 'Values'  # Default y_label

    def generate_data(self):
        """
        Generate bar chart data based on the misleading feature.
        """
        data_gen = DataGenerator()
        if self.misleading_feature == "Inconsistent Time Intervals":
            self.categories, self.values, self.category_type = data_gen.generate_inconsistent_time_series()
            if self.category_type == 'Year':
                self.x_label = 'Years'
            elif self.category_type == 'Month':
                self.x_label = 'Months'
            else:
                self.x_label = 'Time Intervals'
        else:
            self.categories, self.values = data_gen.generate_categorical_data()
            self.category_type = 'Category'
            self.x_label = 'Categories'

        self.data = {'categories': self.categories, 'values': self.values}

    def plot(self):
        """
        Plot the bar chart and apply misleading feature if specified.
        """
        fig_width = 15
        fig_height = 10
        plt.figure(figsize=(fig_width, fig_height))

        bars = plt.bar(range(len(self.categories)), self.values, tick_label=self.categories, width=0.6)  # Set bar width to create spaces
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)

        ax = plt.gca()

        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

        if self.misleading_feature == "Non-Zero Baseline":
            if 'y_start' in self.data:
                self.y_start = self.data['y_start']
            else:
                min_value = min(self.values)
                self.y_start = int(random.uniform(0.2 * min_value, 0.8 * min_value))
            plt.ylim(bottom=self.y_start)
        else:
            self.y_start = 0

        plt.xticks(rotation=45, ha='right')

        apply_bar_style(bars)

    def get_specific_json_data(self):
        """
        Get subclass-specific JSON data for bar chart.
        """
        x_label = ''
        if self.misleading_feature == "Inconsistent Time Intervals":
            if self.category_type == 'Year':
                x_label = 'Years'
            elif self.category_type == 'Month':
                x_label = 'Months'
            else:
                x_label = 'Time Intervals'
        elif self.misleading_feature == "Non-Zero Baseline":
            x_label = ''

        return {
            'y_start': self.y_start if self.misleading_feature == "Non-Zero Baseline" else 0,
            'x_label': x_label,
            'y_label': self.y_label,  # Return the y_label
            'source': self.source
        }

    def get_chart_type(self):
        """
        Return the chart type as 'bar'.
        """
        return 'bar'