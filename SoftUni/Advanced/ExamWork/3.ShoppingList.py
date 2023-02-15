def shopping_list(budget, **items):
    amount = 5
    if 100 > budget:
        return "You do not have enough budget."
    else:
        result = []
        items_list = list(items.items())
        for i in range(len(items_list)):
            item, (price, quantity) = items_list[i]
            if amount > 0:
                price_of_item = price * quantity
                if budget >= price_of_item:
                    result.append(f"You bought {item} for {price_of_item:.2f} leva.")
                    amount -= 1
            else:
                break

        return '\n'.join(result)



# print(shopping_list(100,
#     microwave=(70, 2),
#     skirts=(15, 4),
#     coffee=(1.50, 10),
# ))
#
#
#
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))