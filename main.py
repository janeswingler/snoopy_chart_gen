import tkinter as tk
from gui.gui import ChartApp

def main():
    root = tk.Tk()
    app = ChartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()