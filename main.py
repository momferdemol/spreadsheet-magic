from src.functions import products_per_supplier, inventory_value_per_supplier
from src.helper import load_data

product_list = load_data()

# get dictionary with amount of products per supplier
products_per_supplier = products_per_supplier(product_list)
print(f"\n The amount of products per supplier is {products_per_supplier}\n")

# get dictionary with total inventory value per supplier
inventory_value_per_supplier = inventory_value_per_supplier(product_list)
print(f"\n The total inventory value per supplier is {inventory_value_per_supplier}\n")

