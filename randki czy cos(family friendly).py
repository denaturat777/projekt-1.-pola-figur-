print("Idziemy na randke?")
inp = int(input("ile masz lat?"))
if inp < 18 and inp > 13:
    print("nok")
    print("dobra a baba jestes czy chlop?")
    plec = input()
    if plec == "chlop":
        print("tuff")
        print("rudy jestes?")
        wlosy = input()
        if wlosy == "nie":
             print("noto git")
             print("a lysy jestes w takim razie?")
             lysina = input()
             if lysina == "nie":
                print("fajnie ze posiadasz wlosy")
                print("a grasz w leaugue of legends?")
                grasz = input()
                if grasz == "nie":
                     print("noto spoko")
                else:
                     print("to tym bardziej nie, przeciez ty sie nie myjesz")
             else:
                 print("to tez podziekuje, wracaj do gangu lysego")
        else:
             print("noto podziekuje bo rudym nie mozna ufac")
    else:
         print("sorki ale musze odmowic :(")
else:
    print("eee sory ale ztakim wiekiem to nie za bardzo")