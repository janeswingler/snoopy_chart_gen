import os
import json

def validate_non_zero_baseline(chart):
    if chart['misleading'] and chart['misleading_feature'] == "Non-Zero Baseline":
        if chart['y_start'] == 0:
            return f"Chart {chart['id']} failed: Non-Zero Baseline feature not applied correctly."
    elif not chart['misleading'] and chart['y_start'] != 0:
        return f"Chart {chart['id']} failed: Non-misleading chart with non-zero y-axis start."
    return None

def validate_inconsistent_time_intervals(chart):
    if chart['misleading'] and chart['misleading_feature'] == "Inconsistent Time Intervals":
        if len(chart['data']) <= 2:
            return f"Chart {chart['id']} failed: Not enough data points for Inconsistent Time Intervals."
    return None

def validate_non_sum_to_100(chart):
    if chart['misleading'] and chart['misleading_feature'] == "Non-Sum to 100%":
        total_value = sum(dp["y"] for dp in chart["data"] if dp["y"] is not None)
        if total_value == 100:
            return f"Chart {chart['id']} failed: Total value of pie chart segments is 100."
    return None

def validate_over_segmentation(chart):
    if chart['misleading'] and chart['misleading_feature'] == "Over-Segmentation":
        if len(chart['data']) < 10:
            return f"Chart {chart['id']} failed: Not enough segments for Over-Segmentation."
    elif not chart['misleading'] and len(chart['data']) >= 8:
        return f"Chart {chart['id']} failed: Non-misleading pie chart with too many segments."
    return None

def validate_charts(input_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    processed_charts = data.get("chart", [])
    errors = []

    for chart in processed_charts:
        error = None
        if chart['misleading_feature'] == "Non-Zero Baseline":
            error = validate_non_zero_baseline(chart)
        elif chart['misleading_feature'] == "Inconsistent Time Intervals":
            error = validate_inconsistent_time_intervals(chart)
        elif chart['misleading_feature'] == "Non-Sum to 100%":
            error = validate_non_sum_to_100(chart)
        elif chart['misleading_feature'] == "Over-Segmentation":
            error = validate_over_segmentation(chart)

        if error:
            errors.append(error)

    return errors

def validate_directory(directory):
    all_errors = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f"Validating {filename}...")
            errors = validate_charts(file_path)
            if errors:
                all_errors.extend([f"{filename}: {error}" for error in errors])

    if all_errors:
        print(f"Validation failed for the following charts:\n" + "\n".join(all_errors))
    else:
        print("All charts validated successfully.")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate charts in JSON files within a directory.")
    parser.add_argument("directory", help="Directory containing JSON files with chart data to validate")
    args = parser.parse_args()

    validate_directory(args.directory)

if __name__ == "__main__":
    main()
