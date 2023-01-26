def rectangle(width, length):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:
        def area():
            return width * length
        def perimeter():
            return 2 * (width + length)
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))