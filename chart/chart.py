import json
import uuid
import os
import numpy as np

class Chart:
    """
    Base class for generating and saving chart data.
    """
    def __init__(self, title=''):
        """
        Initialize chart with a title and unique ID.
        """
        self.title = title or ''
        self.chart_id = str(uuid.uuid4())
        self.data = {}

    def generate_data(self):
        """
        Abstract method to generate chart data.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def plot(self):
        """
        Abstract method to plot chart data.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def save_as_json(self, output_dir='chart', misleading=False, misleading_feature=None):
        """
        Save chart data as a JSON file.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        def convert_to_serializable(obj):
            """
            Convert numpy arrays and dicts to serializable formats.
            """
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, dict):
                return {k: convert_to_serializable(v) for k, v in obj.items()}
            return obj

        serializable_data = convert_to_serializable(self.data)

        chart_json = {
            'id': self.chart_id,
            'title': self.title,
            'chart_type': self.get_chart_type(),
            'data': serializable_data,
            'misleading': misleading,
            'misleading_feature': misleading_feature or ''
        }

        chart_json.update(self.get_specific_json_data())

        json_path = os.path.join(output_dir, f'{self.chart_id}.json')
        with open(json_path, 'w') as json_file:
            json.dump(chart_json, json_file, indent=4)

    def get_specific_json_data(self):
        """
        Abstract method to add subclass-specific JSON data.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")