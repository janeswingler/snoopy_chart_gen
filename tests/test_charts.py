import unittest
import numpy as np
from data_generator import DataGenerator

class TestChartData(unittest.TestCase):
    """
    Unit tests for DataGenerator class.
    """
    def setUp(self):
        """
        Set up the DataGenerator instance before each test.
        """
        self.data_gen = DataGenerator()

    def test_generate_time_series_range(self):
        """
        Test that generated time series values are within the specified range.
        """
        categories, values, category_type = self.data_gen.generate_time_series()
        self.assertTrue(all(10 <= v <= 10000000 for v in values), "Values should be within the specified range")

    def test_generate_categorical_data_range(self):
        """
        Test that generated categorical data values are within the specified range.
        """
        categories, values = self.data_gen.generate_categorical_data()
        self.assertTrue(all(10 <= v <= 10000000 for v in values), "Values should be within the specified range")

    def test_type_validation(self):
        """
        Test that the types of generated time series data are correct.
        """
        categories, values, category_type = self.data_gen.generate_time_series()
        self.assertIsInstance(categories, list, "Categories should be a list")
        self.assertIsInstance(values, np.ndarray, "Values should be a numpy array")
        self.assertIsInstance(category_type, str, "Category type should be a string")

    def test_no_duplicates(self):
        """
        Test that generated time series categories do not contain duplicates.
        """
        categories, values, category_type = self.data_gen.generate_time_series()
        self.assertEqual(len(categories), len(set(categories)), "Categories should not contain duplicates")

if __name__ == "__main__":
    unittest.main()