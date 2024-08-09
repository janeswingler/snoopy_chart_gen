import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import matplotlib.pyplot as plt
from chart.bar_chart import BarChart
from chart.line_chart import LineChart
from chart.pie_chart import PieChart
from validate_charts import validate_directory

class ChartApp:
    """
    GUI for generating bar, line, and pie charts with optional misleading features.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Chart Generator")

        self.chart_type_var = tk.StringVar()
        self.misleading_feature_var = tk.StringVar()
        self.num_misleading_var = tk.StringVar()
        self.num_non_misleading_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()
        self.validate_charts_var = tk.BooleanVar()  # Variable to hold the state of the checkbox

        self.create_widgets()
        self.update_misleading_features()

    def create_widgets(self):
        ttk.Label(self.root, text="Chart Type:").grid(row=0, column=0, padx=10, pady=5)
        self.chart_type_combo = ttk.Combobox(self.root, textvariable=self.chart_type_var, state="readonly")
        self.chart_type_combo['values'] = ('bar', 'line', 'pie')
        self.chart_type_combo.grid(row=0, column=1, padx=10, pady=5)
        self.chart_type_combo.bind("<<ComboboxSelected>>", self.update_misleading_features)

        ttk.Label(self.root, text="Misleading Feature:").grid(row=1, column=0, padx=10, pady=5)
        self.misleading_feature_combo = ttk.Combobox(self.root, textvariable=self.misleading_feature_var,
                                                     state="readonly")
        self.misleading_feature_combo.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Misleading Charts:").grid(row=2, column=0, padx=10, pady=5)
        self.num_misleading_entry = ttk.Entry(self.root, textvariable=self.num_misleading_var)
        self.num_misleading_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Non-Misleading Charts:").grid(row=3, column=0, padx=10, pady=5)
        self.num_non_misleading_entry = ttk.Entry(self.root, textvariable=self.num_non_misleading_var)
        self.num_non_misleading_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Output Directory:").grid(row=4, column=0, padx=10, pady=5)
        self.output_dir_entry = ttk.Entry(self.root, textvariable=self.output_dir_var)
        self.output_dir_entry.grid(row=4, column=1, padx=10, pady=5)

        self.output_dir_button = ttk.Button(self.root, text="Browse", command=self.browse_output_directory)
        self.output_dir_button.grid(row=4, column=2, padx=10, pady=5)

        # Add a checkbox for validating charts
        self.validate_charts_checkbox = ttk.Checkbutton(self.root, text="Validate Charts After Generation",
                                                        variable=self.validate_charts_var)
        self.validate_charts_checkbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        ttk.Button(self.root, text="Generate Charts", command=self.start_process).grid(row=6, column=0, columnspan=2,
                                                                                       padx=10, pady=10)

    def browse_output_directory(self):
        output_dir = filedialog.askdirectory()
        if output_dir:
            self.output_dir_var.set(output_dir)

    def update_misleading_features(self, event=None):
        chart_type = self.chart_type_var.get()
        if chart_type == 'bar':
            self.misleading_feature_combo['values'] = ['Non-Zero Baseline', 'Inconsistent Time Intervals']
        elif chart_type == 'line':
            self.misleading_feature_combo['values'] = ['Inconsistent Time Intervals']
        elif chart_type == 'pie':
            self.misleading_feature_combo['values'] = ['Non-Sum to 100%', 'Over-Segmentation']
        else:
            self.misleading_feature_combo['values'] = ['None']
        self.misleading_feature_var.set('None')

    def start_process(self):
        output_dir = self.output_dir_var.get()

        if not output_dir:
            messagebox.showerror("Error", "Output directory must be specified.")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        self.generate_charts(output_dir)

        # If the checkbox is selected, validate the charts
        if self.validate_charts_var.get():
            self.validate_charts(output_dir)

    def generate_charts(self, output_dir):
        chart_type = self.chart_type_var.get()
        misleading_feature = self.misleading_feature_var.get()
        num_misleading = int(self.num_misleading_var.get())
        num_non_misleading = int(self.num_non_misleading_var.get())

        for i in range(num_misleading):
            title = ''  # Set title to an empty string (we will enrich with GPT later)
            self.create_chart(chart_type, misleading_feature, title, output_dir, True)

        for i in range(num_non_misleading):
            title = ''   # Set title to an empty string (we will enrich with GPT later)
            self.create_chart(chart_type, 'None', title, output_dir, False)

        messagebox.showinfo("Success", f"Generated {num_misleading + num_non_misleading} chart in {output_dir}")

    def create_chart(self, chart_type, misleading_feature, title, output_dir, misleading):
        if chart_type == 'bar':
            chart = BarChart(title, misleading_feature)
        elif chart_type == 'line':
            chart = LineChart(title, misleading_feature)
        elif chart_type == 'pie':
            chart = PieChart(title, misleading_feature)
        else:
            return

        chart.generate_data()
        chart.plot()
        # Save the chart image
        image_path = os.path.join(output_dir, f'{chart.chart_id}.png')
        plt.savefig(image_path)
        plt.close()
        # Save the chart JSON
        chart.save_as_json(output_dir, misleading=misleading, misleading_feature=misleading_feature)

    def validate_charts(self, output_dir):
        errors = validate_directory(output_dir)
        if errors:
            messagebox.showerror("Validation Errors", f"Validation failed:\n{errors}")
        else:
            messagebox.showinfo("Validation Success", "All charts validated successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChartApp(root)
    root.mainloop()

