#Aladdin's Gifts
from collections import deque
def check_gifts(product):
    if product <= 199:
        gifts["Gemstone"] += 1
    elif product <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif product <= 399:
        gifts["Gold"] += 1
    elif product <= 499:
        gifts["Diamond Jewellery"] += 1

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))


gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while True:
    if not materials or not magic_levels:
        break
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    product = current_material + current_magic

    if product > 499:
        product /= 2
    if product >= 100:
        check_gifts(product)
        continue
    elif product < 100:
        if product % 2 == 0:
            current_material *= 2
            current_magic *= 3
            product = current_material + current_magic

            if product >= 100:
                check_gifts(product)
                continue
        else:
            product = current_material * 2 + current_magic * 2
            if product >= 100:
                check_gifts(product)
                continue
            else:
                continue





if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
    if materials:
        print(f"Materials left:{', '.join(map(str, materials))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")
    for key in sorted(gifts.keys()):
        if gifts[key] > 0:
            print(f"{key}: {gifts[key]}")

else:
    print("Aladdin does not have enough wedding presents.")
    if materials:
        print(f"Materials left: {', '.join(map(str, materials))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")
    for key in sorted(gifts.keys()):
        if gifts[key] > 0:
            print(f"{key}: {gifts[key]}")

