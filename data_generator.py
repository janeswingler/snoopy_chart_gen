import random
import numpy as np

# Value ranges for datasets
VALUE_RANGES = [
    (10, 100), (100, 1000), (1000, 50000), (50, 500), (200, 2000),
    (500, 10000), (5000, 20000), (10000, 50000), (100000, 1000000),
    (500000, 5000000), (1000000, 10000000)
]


class DataGenerator:
    """
    Class for generating chart datasets with or without specified misleading features.
    """

    def generate_time_series(self):
        """
        Generate a time series dataset for a bar or line chart.
        Returns categories, values, and the category type (Year/Month).
        """
        np.random.seed(random.randint(0, 100))
        start_year = random.randint(1940, 2020)
        intervals = random.choice([
            ([str(year) for year in range(start_year, start_year + 10)], 'Year'),
            (['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December'], 'Month')
        ])

        categories, category_type = intervals

        if category_type == 'Month':
            start_index = random.randint(0, 7)
            end_index = start_index + random.randint(5, 12 - start_index)
            categories = categories[start_index:end_index]

        elif category_type == 'Year':
            start_index = random.randint(0, len(categories) - 10)
            end_index = start_index + random.randint(5, 10)
            categories = categories[start_index:end_index]

        value_range = random.choice(VALUE_RANGES)
        values = np.random.randint(value_range[0], int(value_range[1] * 0.9), len(categories))

        return categories, values, category_type

    def generate_inconsistent_time_series(self):
        """
        Removes a data point from a time series dataset.
        Returns categories, values, and the category type.
        """
        categories, values, category_type = self.generate_time_series()

        if len(categories) > 4:
            remove_index = random.randint(1, len(categories) - 2)  # Remove a data point (but not the first or last)
            categories = categories[:remove_index] + categories[remove_index + 1:]
            values = np.delete(values, remove_index)

        return categories, values, category_type

    def generate_categorical_data(self):
        """
        Generates data for a bar chart with between 2 and 6 categories.
        Returns categories and values.
        """
        num_categories = random.randint(2, 6)
        categories = [f"Category {i + 1}" for i in range(num_categories)]
        value_range = random.choice(VALUE_RANGES)
        values = np.random.randint(value_range[0], int(value_range[1] * 0.9), len(categories))

        return categories, values

    def create_accurate_pie_dataset(self):
        """
        Create a pie chart dataset with values summing to 100%.
        Returns labels and values.
        """
        np.random.seed(random.randint(0, 100))
        num_sections = random.randint(2, 6)  # Number of segments for non-misleading pie chart (2 - 6 segments)
        values = np.random.randint(5, 30, size=num_sections)
        values = values / values.sum() * 100  # Normalize to sum to 100%
        values = np.round(values).astype(int)  # Round to integers
        values[-1] = 100 - values[:-1].sum()  # Adjust last value to ensure sum is 100!
        labels = [f'Section {i + 1}' for i in range(num_sections)]

        return labels, values

    def create_non_100_sum_pie(self):
        """
        Create a pie chart dataset with values not summing to 100%.
        Returns labels and values.
        """
        np.random.seed(random.randint(0, 100))
        num_sections = random.randint(2, 6)
        values = np.random.randint(5, 30, size=num_sections)
        labels = [f'Section {i + 1}' for i in range(num_sections)]

        return labels, values

    def create_oversegmented_pie_dataset(self):
        """
        Create a pie chart dataset with 10 or more segments.
        Returns labels and values.
        """
        np.random.seed(random.randint(0, 100))
        num_sections = random.randint(10, 15)  # An 'over-segmented' pie will for now have 10 or more segments, so as not to crash the model
        values = np.random.randint(5, 30, size=num_sections)
        values = values / values.sum() * 100  # Normalize to sum to 100%
        values = np.round(values).astype(int)  # Round to integers
        values[-1] = 100 - values[:-1].sum()  # Adjust last value to ensure sum is 100!
        labels = [f'Section {i + 1}' for i in range(num_sections)]

        return labels, values