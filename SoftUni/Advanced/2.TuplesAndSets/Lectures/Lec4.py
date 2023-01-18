# Parking Lot
def printPlates(plates):
    if plates:
        for plate in plates:
            print(plate)
    else:
        print("Parking Lot is Empty")


n = int(input())
plates = [input() for _ in range(n)]
parking_data = set()
DIRECTION_IN = 'IN'
DIRECTION_OUT = 'OUT'

for record in plates:
    direction, plate_number = record.split(', ')

    if direction == DIRECTION_IN:
        parking_data.add(plate_number)
    elif direction == DIRECTION_OUT:
        parking_data.remove(plate_number)

printPlates(parking_data)
