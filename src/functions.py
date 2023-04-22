
def products_per_supplier(product_list):
    # calculate the amount of products per supplier
    products_per_supplier = {}
    
    for product_row in range(2, product_list.max_row + 1):

        supplier_name = product_list.cell(product_row, 4).value

        if supplier_name in products_per_supplier:
            current_num_products = products_per_supplier[supplier_name]
            products_per_supplier[supplier_name] = current_num_products + 1

        else:
            products_per_supplier[supplier_name] = 1

    return products_per_supplier


def inventory_value_per_supplier(product_list):
    # calculate the total inventory value per supplier
    inventory_value_per_supplier = {}

    for product_row in range(2, product_list.max_row + 1):

        supplier_name = product_list.cell(product_row, 4).value
        inventory = product_list.cell(product_row, 2).value
        price = product_list.cell(product_row, 3).value

        if supplier_name in inventory_value_per_supplier:
            current_value_per_supplier = inventory_value_per_supplier[supplier_name]
            inventory_value_per_supplier[supplier_name] = current_value_per_supplier + inventory * price

        else:
            inventory_value_per_supplier[supplier_name] = inventory * price

    return inventory_value_per_supplier