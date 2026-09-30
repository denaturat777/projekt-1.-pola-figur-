pi = 3.14

print("Bryly - a | Plaskie - b | Inne wzory - c")
inp = input("inp: ").lower().strip()

# Bryly 

if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    
    # Pola powierzchni bryl
    if inp == "a":
        print("szescan - a | prostopadloscan - b | graniastoslup - c | ostroslup - d | walec - e | stozek - f | kula - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a = float(input("a = "))
            print(f"ppSzecianu = {6 * a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu = {2*a*b + 2*a*c + 2*b*c}")
        elif inp == "c":
            pp = float(input("Pp = "))
            pb = float(input("Pb = "))
            print(f"ppGraniastoslupa = {2 * pp + pb}")
        elif inp == "d":
            pp = float(input("Pp = "))
            pb = float(input("Pb = "))
            print(f"ppOstroslupa = {pp + pb}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"ppWalca = {2 * pi * r**2 + 2 * pi * r * h}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"ppStozka = {pi * r**2 + pi * r * l}")
        elif figura == "g" or inp == "g":  # Poprawione dla bezpieczeństwa
            r = float(input("r = "))
            print(f"ppKuli = {4 * pi * r**2}")
        else:
            print("Nie ma takiej komendy: ")
            
    # Obetsci bryl
    elif inp == "b":
        print("vSzecianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a = float(input("a = "))
            print(f"vSzecianu = {a**3}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProstopadloscianu = {a * b * c}")
        elif inp == "c":
            pp = float(input("Pp = "))
            h = float(input("H = "))
            print(f"vGraniastoslupa = {pp * h}")
        elif inp == "d":
            pp = float(input("Pp = "))
            h = float(input("H = "))
            print(f"vOstroslupa = {(1/3) * pp * h}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"vWalca = {pi * r**2 * h}")
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"vStozka = {(1/3) * pi * r**2 * h}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli = {(4/3) * pi * r**3}")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")

# Figury Plaskie

elif inp == "b":
    print("obwody fig plaskich - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    
    # Obwody
    if inp == "a":
        print("kwadrat - a | prostokat/rownoleglobok - b | trapez - c | trojkat - d | trojkat rownoboczny - e | kolo - f | romb - g")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"Obwod kwadratu = {4 * a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"Obwod = {2 * a + 2 * b}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"Obwod trapezu = {a + b + c + d}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"Obwod trojkata = {a + b + c}")
        elif inp == "e":
            a = float(input("a = "))
            print(f"Obwod trojkata rownobocznego = {3 * a}")
        elif inp == "f":
            r = float(input("r = "))
            print(f"Obwod kola = {2 * pi * r}")
        elif inp == "g":
            a = float(input("a = "))
            print(f"Obwod rombu = {4 * a}")
        else:
            print("nie ma takiej komendy")
            
    # Pola powierzchni
    elif inp == "b":
        print("kwadrat - a | prostokat - b | rownoleglobok/romb(h) - c | trapez - d | trojkat - e | trojkat rownoboczny - f | kolo - g | romb(ef) - h")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"Pole kwadratu = {a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"Pole prostokata = {a * b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"Pole = {a * h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"Pole trapezu = {((a + b) * h) / 2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"Pole trojkata = {0.5 * a * h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"Pole trojkata rownobocznego = {(a**2 * math.sqrt(3)) / 4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"Pole kola = {pi * r**2}")
        elif inp == "h":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"Pole rombu = {(e * f) / 2}")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")
