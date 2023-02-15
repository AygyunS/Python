def even_odd(*args):
    command = args[-1]
    result = []

    for n in args[:-1]:
        if int(n) % 2 == 0 and command == "even":
            result.append(int(n))
        elif int(n) % 2 == 1 and command == 'odd':
            result.append(int(n))

    return result

def even_odd2(*args):
     command = args[-1]

     if command == 'even':
         return [n for n in args[:-1] if n % 2 == 0]
     elif command == 'odd':
         return [n for n in args[:-1] if n % 2 == 1]

print(even_odd2(1, 2, 3, 4, 5, 6, "even"))
