from src.functions import products_per_supplier
from src.helper import load_data

product_list = load_data()

products_per_supplier = products_per_supplier(product_list)
print(f"\n The amount of products per supplier is {products_per_supplier}\n")

