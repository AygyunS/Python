def concatenate(*names, **kwargs):
    output = ''.join(names)

    for key in kwargs:
        output = output.replace(key, kwargs[key])

    return output

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))