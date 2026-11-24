import funkcje.plaskie as pl
import funkcje.warunki_tr as tr
import funkcje.bryly as br

def legenda()->None:
    print("a - bryly")
    print("b - plaskie")
    print("c - warunki tr")
    print("e - wyjdz z programu")

def main()->None:
    while True:
        legenda()
        inp = input().lower().strip()
        if inp == "a":
            br.bryly()
        elif inp == "b":
            pl.plaskie()
        elif inp == "c":
            tr.trojkaty()
        elif inp ==  "e":
            print("program zakonczyl dzialanie")
            break
        else:
            "n ma takiej komendy sr"

#------------------------------------------------------------------------

bryly.py

from math import pi as PI

# pc bryl

def pc_szescianu(a:float)->float:
    return a*a**2

def pc_prostopadloscianu(a:float,b:float,c:float)->float:
    return 2**a*b + 2**b*c

def pc_graniastoslupa(pb:float,pp:float)->float:
    return 2*pp + pb

def pc_ostroslupa(pb:float,pp:float)->float:
    return pb+pp

def pc_walca(r:float,h:float)->float:
    return 2*PI*r**2 + 2*PI*r*h

def pc_stozka(r:float,l:float)->float:
    return PI*r*r + PI*r*l

def pc_kuli(r:float)->float:
    return a*PI**r*r

def legenda_pc()->None:
    print("a - pc_szescianu")
    print("b - pc_prostopadloscianu")
    print("c - pc_graniastoslupa")
    print("d - pc_ostroslupa")
    print("e - pc_walca")
    print("f - pc_stozka")
    print("g - pc_kuli")

def pc_bryl()->None:
    legenda_pc()
    inp = input().lower().strip()
    if inp == "a":
        a = float(input("a: "))
        print(f"dla szescianu o krawedzi {a} pc = {pc_szescianu(a)}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"dla prostopadloscianu o krawedziach {a} {b} {c} pc = {pc_prostopadloscianu(a,b,c)}")
    elif inp == "c":
        pp = float(input("pp: "))
        pb = float(input("pb: "))
        print(f"dla graniastoslupa z pp {pp} i pb {pb} pc = {pc_graniastoslupa(pb,pp)}")
    elif inp == "d":
        pp = float(input("pp: "))
        pb = float(input("pb: "))
        print(f"dla ostroslupa z pp {pp} i pb {pb} pc = {pc_ostroslupa(pb,pp)}")
    elif inp == "e":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"dla walca z r {r} i h {h} pc = {pc_walca(r,h)}")
    elif inp == "f":
        r = float(input("r: "))
        l = float(input("l: "))
        print(f"dla stozka z r {r} i l {l} pc = {pc_stozka(r,l)}")
    elif inp == "g":
        r = float(input("r: "))
        print(f"dla kuli z r {r} pc = {pc_kuli(r)}")
    else:
        print("n ma takiej komendy")


# objetosci bryl

def obj_szescianu(a:float)->float:
    return a**3

def obj_prostopadloscianu(a:float,b:float,c:float)->float:
    return a*b*c

def obj_graniastoslupa(pp:float,h:float)->float:
    return pp*h

def obj_ostroslupa(pp:float,h:float)->float:
    return pp*h/3

def obj_walca(r:float,h:float)->float:
    return PI*r*r*h

def obj_stozka(r:float,h:float)->float:
    return PI*r*r*h/3

def obj_kuli(r:float)->float:
    return PI*r*r*r*1.25

def legenda_pc()->None:
    print("a - obj_szescianu")
    print("b - obj_prostopadloscianu")
    print("c - obj_graniastoslupa")
    print("d - obj_ostroslupa")
    print("e - obj_walca")
    print("f - obj_stozka")
    print("g - obj_kuli")

def obj_bryl()->None:
    legenda_obj()
    inp = input().lower().strip()
    if inp == "a":
        a = float(input("a: "))
        print(f"dla szescianu o krawedzi {a} pc = {pc_szescianu(a)}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"obj prostopadloscianu o podanych krawedziach wynosi {obj_prostopadloscianu(a,b,c)}")
    elif inp == "c":
        pp = float(input("pp: "))
        h = float(input("h: "))
        print(f"obj graniastoslupa  wynosi {obj_graniastoslupa(pp,h)}")
    elif inp == "d":
        pp = float(input("pp: "))
        h = float(input("h: "))
        print(f"obj ostroslupa  wynosi {obj_ostroslupa(pp.h)}")
    elif inp == "e":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"dobj walca wynosi {obj_walca(r,h)}")
    elif inp == "f":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"obj stozka wynosi {obj_stozka(r,h)}")
    elif inp == "g":
        r = float(input("r: "))
        print(f"obj kuli wynosi {obj_kuli(r)}")
    else:
        print("n ma takiej komendy")

#---------------------------------------------------------------------

def bryly()->None:
    print("a - pc bryl")
    print("b - obj bryl")
    inp = input().lower().strip()
    if inp == "a":
        pc_bryl()
    elif inp == "b":
        obj_bryl()
    else:
        print("n ma takiej komendy")


#figury plaskie

# pola pp

def obj_kwadratu(a:float)->float:
    return a**2

def obj_prostokota(a:float,b:float)->float:
    return a*b

def obj_rownolegloboku(a:float,h:float)->float:
    return a*h

def obj_trapezu(a:float,b:float,h:float)->float:
    return (a+b)*h/2

def legenda_pp()->None:
    print("a - pp_kwadratu")
    print("b - pp_prostokota")
    print("c - pp_rownolegloboku")
    print("d - pp_trapezu")
    print("e - pp_trojkota")
    print("f - pp_kola")
    print("g - pp_rombu")

def pola_pp()->None:
    legenda_pp()
    inp = input().lower().strip()
    if inp == "a":
        a = float(input("a: "))
        print(f"dla kwadratu o boku {a} pp = {pp_kwadratu(a)}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"dla prostotkota o bokach {a} i {b} pp = {pp_prostokota(a,b)}")
    elif inp == "c":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla rownolegloboku o boku {a} i {h} pp = {pp_rownolegloboku(a,h)}")
    elif inp == "d":
        a = float(input("a: "))
        b = float(input("b: "))
        h = float(input("h: "))
        print(f"dla trapezu o bokach {a} i {b} i {h} pp = {pp_trapezu(a,b,h)}")
    elif inp == "e":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla trojkota o podstawie {a} i wysokosci {h} pp = {pp_trojkota(a,h)}")
    elif inp == "f":
        r = float(input("r: "))
        print(f"pp kola o promieniu {r} pp = {pp_kola(r)}")
    elif inp == "g":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla rombu o podstawie {a} i wysokosci {h} pp = {pp_rombu(a,h)}")
    else:
        print("n ma takiej komendy")

#-------------------------------------------------------------------------------

# obwody

def obw_kwadratu(a:float)->float:
    return 4*a

def obw_prostokota(a:float,b:float)->float:
    return 2**a+2*b

def obw_rownolegloboku(a:float,b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float,b:float,c:float,d:float)->float:
    return a + b + c + d

def obw_trojkota(a:float,b:float,c:float)->float:
    return a+b+c

def obw_kola(r:float)->float:
    return 2*PI*r

def obw_rombu(a:float)->float:
    return 4*a

def legenda_pc()->None:
    print("a - obw_kwadratu")
    print("b - obw_prostokota")
    print("c - obw_rownolegloboku")
    print("d - obw_trapezu")
    print("e - obw_trojkota")
    print("f - obw_kola")
    print("g - obw_rombu")

def obwody()->None:
    legenda_obw()
    inp = input().lower().strip()
    if inp == "a":
        a = float(input("a: "))
        print(f"dla kwadratu o boku {a} obw = {obw_kwadratu(a)}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"dla prostotkota o bokach {a} i {b} obw = {obw_prostokota(a,b)}")
    elif inp == "c":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"dla rownolegloboku o bokach {a} {b} obw = {obw_rownolegloboku(a,b)}")
    elif inp == "d":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = float(input("d: "))
        print(f"dla trapezu o bokach {a} {b} {c} {d} obw = {obw_trapezu(a,b,c,d)}")
    elif inp == "e":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"dla trojkota o bokach {a} {b} {c} obw = {obw_trojkota(a,h)}")
    elif inp == "f":
        r = float(input("r: "))
        print(f"pp kola o promieniu {r} obw = {obw_kola(r)}")
    elif inp == "g":
        a = float(input("a: "))
        print(f"dla rombu o boku {a} obw = {obw_rombu(a)}")
    else:
        print("n ma takiej komendy")


#--------------------------------------------------------------------------------

def plaskie()->None:
    print("wzory na figury plaskie")
    print("a - pola pp")
    print("b - obwody")
    inp = input().lower().strip()
    if inp == "a":
        pola_pp()
    elif inp == "b":
        obwody()
    else:
        print("n ma takiej komendy")


# warunki trojkotow

def czy_mg_zrobic_tr(a:float,b:float,c:float)->str:
    if a+b>c and c+b>a and c+a>b:
        return "tak"
    else:
        return "nie"

#-------------------------------------------------------------------------------

def trojkoty()->bool:
    print("czy trojkot o danych bokach istnieje?")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    czy_mg_zrobic_tr(a,b,c)
