from typing import Self

def romanToInt(self, s: str) -> int:
    
    sum = 0
    for i in inp:
        if i == "I":
            sum+=1
        elif i == "V":
            sum+=5
        if i == "X":
            sum+=10
        elif i == "L":
            sum+=50
        if i == "C":
            sum+=100
        elif i == "D":
            sum+=500
        elif i == "M":
            sum+=1000
    return sum
inp = input()
print(romanToInt(Self, inp))