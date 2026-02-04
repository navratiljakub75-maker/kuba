print("Zadej první číslo:")
cislo1 = float(input())
print("Zadej druhé číslo")
cislo2 = float(input())
print("Zadej operaci (+,*,/,-,cos,sin,tan):")
operace = input()
if operace == "+":
    vysledek = cislo1 + cislo2
    print(vysledek)
else:
    if operace == "-":
        vysledek = cislo1 - cislo2
        print(vysledek)
    else:
        if operace == "*":
            vysledek = cislo1 * cislo2
            print(vysledek)
        else:
            if operace == "/":
                vysledek = cislo1 / cislo2
                print(vysledek)
            else:
                if operace == "sin":
                    rad = cislo1 * math.pi / 180
                    vysledek = sin(rad)
                    print(vysledek)
                else:
                    if operace == "cos":
                        rad = cislo1 * math.pi / 180
                        vysledek = cos(rad)
                        print(vysledek)
                    else:
                        if operace == "tan":
                            rad = cislo1 * math.pi / 180
                            vysledek = tan(rad)
                            print(vysledek)
                        else:
