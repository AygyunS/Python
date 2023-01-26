def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
        return result
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return 0
            result /= num
        return result


print(operate('/', 1, 2, 0))