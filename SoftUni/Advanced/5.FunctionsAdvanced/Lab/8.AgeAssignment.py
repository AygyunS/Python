def age_assignment(*names, **data):
    result = []
    output = ''

    for name in names:
        result.append((name, data[name[0]]))
    result.sort(key=lambda x: x[0])

    for name, age in result:
        output += f"{name} is {age} years old.\n"

    return output


def age_assignment2(*names, **data):
    result = sorted((name, data[name[0]]) for name in names)
    return '\n'.join(f"{name} is {age} years old." for name, age in result)

print(age_assignment2("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))