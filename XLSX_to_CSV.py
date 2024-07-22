import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def convert_xlsx_to_csv(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(directory, filename)
            # Load the .xlsx file
            excel_data = pd.read_excel(file_path)
            # Remove the .xlsx extension and add .csv
            csv_filename = filename.replace('.xlsx', '.csv')
            csv_path = os.path.join(directory, csv_filename)
            # Save as .csv with UTF-8 encoding
            excel_data.to_csv(csv_path, index=False, encoding='utf-8')
            print(f"Converted {filename} to {csv_filename}")

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        convert_xlsx_to_csv(folder_selected)
    else:
        print("No directory selected!")

if __name__ == "__main__":
    select_directory()
