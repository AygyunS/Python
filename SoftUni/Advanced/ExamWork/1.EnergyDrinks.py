from collections import deque

milligrams_caffeine = deque(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

total_caffeine = 0

while len(milligrams_caffeine) > 0 and len(energy_drinks) > 0:

    current_caffeine = milligrams_caffeine.pop()
    current_drink = energy_drinks.popleft()

    caffeine = current_caffeine * current_drink

    if caffeine + total_caffeine <= 300:
        total_caffeine += caffeine
    else:
        energy_drinks.append(current_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: { ', '.join(map(str, energy_drinks)) }")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")

# caffeine = [int(x) for x in input().split(", ")]
# drinks = [int(x) for x in input().split(", ")]
# total_caffeine = 0
#
# while len(caffeine) > 0 and len(drinks) > 0:
#     current_caffeine = caffeine.pop()
#     current_drink = drinks.pop(0)
#     total_caffeine += current_caffeine * current_drink
#
#     if total_caffeine > 300:
#         total_caffeine -= 30
#         drinks.append(current_drink)
#
# if len(drinks) > 0:
#     print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
# else:
#     print("At least Stamat wasn't exceeding the maximum caffeine.")
#
# print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")