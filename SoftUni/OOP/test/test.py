class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# You can call static methods without creating an instance of the class
# result1 = MathUtils.add(2, 3)
# result2 = MathUtils.multiply(3, 4)
# print(result1)  # Output: 5
# print(result2)  # Output: 12
print(MathUtils.add(2, 3))
