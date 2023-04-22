from src.functions import products_per_supplier, inventory_value_per_supplier, product_inventory_under_10, calculate_inventory_value_per_product
from src.helper import load_data, save_data

inventory_file = load_data()

# get dictionary with amount of products per supplier
products_per_supplier = products_per_supplier(inventory_file)
print(f"\n The amount of products per supplier is {products_per_supplier}\n")

# get dictionary with total inventory value per supplier
inventory_value_per_supplier = inventory_value_per_supplier(inventory_file)
print(f"\n The total inventory value per supplier is {inventory_value_per_supplier}\n")

# get dictionary with products where inventory is less then 10
product_inventory_under_10 = product_inventory_under_10(inventory_file)
print(f"\n Inventory count less then 10 for product {product_inventory_under_10}\n")

# calculate inventory value per product and add to worksheet
product_list = calculate_inventory_value_per_product(inventory_file)
print("\n Inventory value per product calculated and added to worksheet\n")

# save new version of worksheet to output folder in project
save_data = save_data(inventory_file)
print(f"\n Result for saving new inventory is {save_data}\n")
