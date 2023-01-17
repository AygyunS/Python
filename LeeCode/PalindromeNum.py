
from typing import Self

class Solution:
    num = input()
    def isPalindrome(self, x: int) -> bool:
        numList = [i for i in str(x)]
        return numList == numList[::-1]

    print(isPalindrome(Self, num))
