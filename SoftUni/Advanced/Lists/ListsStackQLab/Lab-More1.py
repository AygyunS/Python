# str_nums = input()

# nums = str_nums.split()

# nums = [int(n) for n in nums]

# odd_nums = [x for x in nums if x % 2 == 0]

# print(", ".join([str(n) for n in odd_nums]))


nums = [1, 2, 3, 4, 5]
# result = sum(nums)
# print(result)
# 15

# for idx, val in enumerate(nums, start=1):
#     print(idx, val)
# (prints index and value)

a = [1, 2, 3, 4, 5, 6, 7]
b = ["a", "b", "c", "d", "e"]

for val1, val2 in zip(a, b):
    print(val1, val2)
# if you put strict=True the program returns error with lengths not matching
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
