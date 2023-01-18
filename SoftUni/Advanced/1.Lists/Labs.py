# input = input()
# li = list(input.split(" "))
# li.reverse()
# print(*li)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
if "banana" in y:
    y.insert(y.index("banana") + 1,"orange")	
thistuple = tuple(y)

print(thistuple)
