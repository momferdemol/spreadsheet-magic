import openpyxl

def load_data():

    inventory_file = openpyxl.load_workbook("./input/inventory.xlsx")
    raw_data = inventory_file["DataSheet"]
    return raw_data