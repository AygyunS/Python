# str_nums = input()
# numbers = str_nums.split()

# result = int(numbers[0])

# for i in range(1, len(numbers), 2):
#     if numbers[i] == "+":
#         result += int(numbers[i+1])
#     elif numbers[i] == "-":
#         result -= int(numbers[i+1])

# print(result)

# from collections import deque

# nums = deque()

# map_functions = {
#     1: lambda x: nums.append(x[1]),
#     2: lambda x: nums.pop() if nums else None,
#     3: lambda x: print(max(nums)),
#     4: lambda x: print(min(nums))
# }

# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)

# nums.reverse()

# print(*nums, sep=", ")
