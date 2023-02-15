def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []

    for kwargs, quantity in kwargs:
        result.append(f"{kwargs}: {quantity}")

    return '\n'.join(result)

def grocery_store2(**kwargs):
    return '\n'.join([f"{kwargs}: {quantity}" for kwargs, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))])

print(grocery_store2(
    bread=5,
    pasta=12,
    eggs=12,
))
