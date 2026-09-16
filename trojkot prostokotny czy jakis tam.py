a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and a + c > b:
    print("moge zbudować tr")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 == c**2 == b**2:
        print("to jest tr prostokątny")
    else:
        print("to n jest tr prostokątny")
else:
    print("nie mg zbudować tr")
