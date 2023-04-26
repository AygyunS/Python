class vowels:
    def __init__(self, my_str: str):
        self.my_str = my_str
        self.index = 0


    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.my_str):
            char = self.my_str[self.index]
            self.index += 1
            if char in 'aeiouAEIOU':
                return char
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
