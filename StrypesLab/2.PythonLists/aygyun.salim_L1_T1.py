import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    print("special case")
else:
    d = b**2 - 4*a*c  # дискриминантата
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print(f"{x1}|{x2}")
    elif d == 0:
        x1 = -b / (2*a)
        print(f"{x1}")
    else:
        print("no real roots")
