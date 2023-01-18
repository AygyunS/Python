#1. Numbers
# input the first sequence of numbers
first_sequence = set(map(int, input().split()))
# input the second sequence of numbers
second_sequence = set(map(int, input().split()))

# input the number of commands
n = int(input())

# process the commands
for i in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence.update(map(int, command[2:]))
        elif command[1] == "Second":
            second_sequence.update(map(int, command[2:]))
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence.difference_update(map(int, command[2:]))
        elif command[1] == "Second":
            second_sequence.difference_update(map(int, command[2:]))
    elif command[0] == "Check":
        if command[1] == "Subset":
            if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
                print("True")
            else:
                print("False")

# print the final sequences
print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))
