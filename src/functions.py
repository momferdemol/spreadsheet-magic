

def products_per_supplier(inventory_file):
    # calculate the amount of products per supplier

    worksheet = inventory_file["DataSheet"]

    products_per_supplier = {}
    
    for product_row in range(2, worksheet.max_row + 1):

        supplier_name = worksheet.cell(product_row, 4).value

        if supplier_name in products_per_supplier:
            current_num_products = products_per_supplier[supplier_name]
            products_per_supplier[supplier_name] = current_num_products + 1

        else:
            products_per_supplier[supplier_name] = 1

    return products_per_supplier


def inventory_value_per_supplier(inventory_file):
    # calculate the total inventory value per supplier

    worksheet = inventory_file["DataSheet"]

    inventory_value_per_supplier = {}

    for product_row in range(2, worksheet.max_row + 1):

        supplier_name = worksheet.cell(product_row, 4).value
        inventory = worksheet.cell(product_row, 2).value
        price = worksheet.cell(product_row, 3).value

        if supplier_name in inventory_value_per_supplier:
            current_value_per_supplier = inventory_value_per_supplier[supplier_name]
            inventory_value_per_supplier[supplier_name] = current_value_per_supplier + inventory * price

        else:
            inventory_value_per_supplier[supplier_name] = inventory * price

    return inventory_value_per_supplier


def product_inventory_under_10(inventory_file):
    # return products with current inventory under 10 items

    worksheet = inventory_file["DataSheet"]

    product_inventory_under_10 = {}

    for product_row in range(2, worksheet.max_row + 1):

        product_num = worksheet.cell(product_row, 1).value
        inventory = worksheet.cell(product_row, 2).value

        if inventory < 10:
            product_inventory_under_10[product_num] = inventory
    
    return product_inventory_under_10


def calculate_inventory_value_per_product(inventory_file):
    # return inventory value per product

    worksheet = inventory_file["DataSheet"]

    for product_row in range(2, worksheet.max_row + 1):

        inventory = worksheet.cell(product_row, 2).value
        price = worksheet.cell(product_row, 3).value
        inventory_price = worksheet.cell(product_row, 5)

        inventory_price.value = inventory * price

    return inventory_file
