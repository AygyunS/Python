
# Create a list to store the opening parentheses
import sys
stack = []

# Read the input sequence of parentheses
s = input()

# Iterate over the characters in the input string
for c in s:
    # If the character is an opening parenthesis, append it to the stack
    if c in ['(', '[', '{']:
        stack.append(c)
    # If the character is a closing parenthesis
    elif c in [')', ']', '}']:
        # If the stack is empty, the parentheses are not balanced
        # because there is no corresponding opening parenthesis
        if not stack:
            print("NO")
            break
        # If the closing parenthesis does not correspond to the
        # most recent opening parenthesis, the parentheses are not balanced
        elif (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
            print("NO")
            break
        # If the closing parenthesis corresponds to the most recent opening parenthesis,
        # remove the opening parenthesis from the stack
        else:
            stack.pop()

# If the loop ends without finding any unbalanced parentheses, the parentheses are balanced
# because the stack should be empty at this point
else:
    print("YES")

# Exit the program
sys.exit()
