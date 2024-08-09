# Chart Data Generator and Validator

This repository contains a Python program designed to programmatically generate and validate chart data. The main objective is to create various types of charts—bar, line, and pie charts—with customizable features, including misleading attributes. Additionally, the program provides a GUI for ease of use, including an option to validate the generated charts.

## Directory Structure
```
chart-data-generator/
│
├── chart
│ ├── bar_chart.py
│ ├── chart.py
│ ├── line_chart.py
│ ├── pie_chart.py
│
├── gui
│ ├── gui.py
│
├── style
│ ├── bar_styles.py
│ ├── common_styles.py
│ ├── line_styles.py
│ ├── pie_styles.py
│
├── tests
│ ├── test_charts.py
│
├── init.py
├── data_generator.py
├── main.py
├── requirements.txt
├── setup.py
├── validate_charts.py
└── README.md
```
## Files Overview

- `main.py`: The main entry point for the program. Launches the GUI for chart generation and validation.
- `data_generator.py`: Handles the core logic for generating chart data.
- `validate_charts.py`: Contains functions to validate generated charts by checking for specific misleading features, such as non-zero baselines, inconsistent time intervals, non-sum to 100% in pie charts, and over-segmentation, ensuring that the charts adhere to the expected formats and criteria.
- `gui.py`: Provides a graphical user interface for interacting with the chart generation and validation process.
- `bar_chart.py`: Contains the logic specific to generating vertical bar charts.
- `chart.py`: A base class that defines the common structure and behavior for all charts.
- `line_chart.py`: Contains the logic specific to generating line charts.
- `pie_chart.py`: Contains the logic specific to generating pie charts.
- `test_charts.py`: Includes test cases to ensure the functionality of the DataGenerator class, specifically verifying that generated time series and categorical data are within specified ranges, checking data types, and ensuring that there are no duplicate categories in the generated data.
- `bar_styles.py`: Manages different styles that can be applied to bar charts for variety.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This program requires Python 3.x. Additionally, you'll need to install the necessary dependencies.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/janeswingler/snoopy_chart_generator.git
    cd snoopy_chart_generator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the package in editable mode:
    ```bash
    pip install -e .
    ```

### Usage

#### Command-Line Usage

To generate charts via the command line, you can run:

```bash
chart_gen /path/to/your/directory