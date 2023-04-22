import openpyxl
from datetime import datetime


def load_data():
    # load spreadsheet
    inventory_file = openpyxl.load_workbook("./input/inventory.xlsx")
    return inventory_file


def save_data(inventory_file):
    # save spreadsheet as file with new data to output folder
    isFileSaved = True
    try:
        today_date = datetime.today().strftime('%d-%m-%Y %H.%M')
        filepath = f"./output/inventory {today_date}.xlsx"
        inventory_file.save(filepath)
    except ValueError:
        isFileSaved = False
        SystemExit
    
    return isFileSaved
