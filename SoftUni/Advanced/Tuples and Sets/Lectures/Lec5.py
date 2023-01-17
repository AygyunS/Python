# SoftUni Party
n = int(input())

persons = set(input() for _ in range(n))
afterList = set()

while True:
    person = input()
    if person == "END":
        break
    else:
        afterList.add(person)

diffrences = [x for x in persons if x not in afterList]

print(len(diffrences))
sortElements = sorted(diffrences)


print('\n'.join(sortElements))
