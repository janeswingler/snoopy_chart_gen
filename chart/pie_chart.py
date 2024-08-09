import matplotlib.pyplot as plt
import random
import numpy as np
from data_generator import DataGenerator
from styles.pie_styles import apply_pie_style
from chart.chart import Chart

class PieChart(Chart):
    """
    Class for generating and plotting pie chart with optional misleading features.
    """
    pie_count = 0  # Class variable to keep track of pie chart count for id's

    def __init__(self, title='', misleading_feature=None, source=''):
        """
        Initialize pie chart with title, misleading feature, and source.
        """
        super().__init__(title)
        self.misleading_feature = misleading_feature
        self.source = source  # Store the source
        PieChart.pie_count += 1
        self.chart_id = f"pie{PieChart.pie_count}"

    def generate_data(self):
        """
        Generate pie chart data based on the misleading feature.
        """
        data_gen = DataGenerator()
        if self.misleading_feature == "Non-Sum to 100%":
            self.labels, self.sizes = data_gen.create_non_100_sum_pie()
        elif self.misleading_feature == "Over-Segmentation":
            self.labels, self.sizes = data_gen.create_oversegmented_pie_dataset()
        else:
            self.labels, self.sizes = data_gen.create_accurate_pie_dataset()

        self.data = {'labels': self.labels, 'sizes': self.sizes}

    def plot(self):
        """
        Plot the pie chart and apply misleading feature if specified.
        """
        fig_width = 12
        fig_height = 12
        plt.figure(figsize=(fig_width, fig_height))

        # Custom autopct function to use the original sizes for the labels!!
        def custom_autopct(values):
            def inner_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return f'{val}'
            return inner_autopct

        wedges, texts, autotexts = plt.pie(
            self.sizes, labels=self.labels, autopct=custom_autopct(self.sizes)
        )
        plt.title(self.title)
        apply_pie_style(wedges, texts, autotexts)

    def get_specific_json_data(self):
        """
        Get subclass-specific JSON data for pie chart.
        """
        return {
            'x_label': '',
            'y_label': ''
        }

    def get_chart_type(self):
        """
        Return the chart type as 'pie'.
        """
        return 'pie'