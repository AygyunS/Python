from collections import deque

first = input().split(", ")
second = deque(map(int, input().split(", ")))
third = deque(map(int, input().split(", ")))

taken_seats = []
counter = 0

while counter < 10 and len(taken_seats) < 3:
    current_second = second.popleft()
    current_third = third.pop()

    seat_char = chr(current_second + current_third)
    first_seat = f"{current_second}{seat_char}"
    second_seat = f"{current_third}{seat_char}"
    counter += 1
    if first_seat in first:
        first.remove(first_seat)
        taken_seats.append(first_seat)
        continue
    elif second_seat in first:
        first.remove(second_seat)
        taken_seats.append(second_seat)
        continue
    else:
        second.append(current_second)
        third.appendleft(current_third)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {counter}")
