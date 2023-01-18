# # Count Same Values - first version
# numbers = tuple(map(float, input().split()))

# nums = {}

# for num in numbers:
#     if num not in nums:
#         nums[num] = 0
#     nums[num] += 1

# [print(f"{key} - {value} times") for key, value in nums.items()]

# second version
values = tuple(map(float, input().split(' ')))
count_value = {value: values.count(value) for value in values}

values_counter = {}

for value in values:
    if value not in values_counter:
        values_counter[value] = 0
    values_counter[value] += 1

for k, v in count_value.items():
    print(f"{k} - {v} times")

# third version shortest
# values = tuple(map(float, input().split(' ')))
# count_value = {value: values.count(value) for value in values}

# for k, v in count_value.items():
#     print(f"{k} - {v} times")
