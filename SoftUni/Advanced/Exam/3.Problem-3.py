def shop_from_grocery_list(budget, products, *args):
    result = []

    for product in args:
        product_name, price = product
        if price <= budget:
            if product_name in products:
                budget -= price
                result.append(product_name)
                products.remove(product_name)
        else:
            break

        if not products:
            break

    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        return f"You did not buy all the products. Missing products: {', '.join([str(x) for x in products])}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))