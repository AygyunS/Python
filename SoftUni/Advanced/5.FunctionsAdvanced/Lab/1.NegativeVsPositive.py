
def neg_pos(nums):
    neg = 0
    pos = 0

    for num in nums:
        if num < 0:
            neg += int(num)
        else:
            pos += int(num)
    return neg, pos


nums = [int(x) for x in input().split()]

print(neg_pos(nums)[0])
print(neg_pos(nums)[1])

if abs(neg_pos(nums)[0]) <= neg_pos(nums)[1]:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
# shorter solution:
pos_nums = sum(n for n in nums if n > 0)
neg_nums = sum(n for n in nums if n < 0)

