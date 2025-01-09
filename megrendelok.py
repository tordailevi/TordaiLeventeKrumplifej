from Beolvaso import Beolvaso

def filebeolvasas():
    megrendeles_lista = []
    file = open("megrendelok.txt", "r", encoding='UTF-8')
    elso_sor = file.readline()
    tobbi_sor_lista = file.readlines()
    for i in range(0, len(tobbi_sor_lista), 1):
        sor = tobbi_sor_lista[i].strip()
        sor_lista = sor.split("$")
        rendeles = Beolvaso(sor_lista[0], sor_lista[1], sor_lista[2])
        megrendeles_lista.append(rendeles)
    file.close()
    return megrendeles_lista

def rendelesszam(megrendeles_lista):
    print("III/A, B:")
    print(len(megrendeles_lista))

def krumplifej(megrendeles_lista):
    for i in range(0, len(megrendeles_lista), 1):
        if megrendeles_lista[i].emailcim == "krumplifej@citromail.hu":
            szamlalo:int = 0
    print("III/C:")
    print(f"A krumplifej@citrmail.hu címhez tartozó megrendelések száma: {szamlalo}")

def legutolso_rendeles(megrendeles_lista):
    legnagyobb = megrendeles_lista[0]
    for i in range(0, len(megrendeles_lista), 1):
        if megrendeles_lista[i].rendeles_szama > legnagyobb.rendeles_szama:
            legutolso_email = megrendeles_lista[i].emailcim
            legnagyobb = megrendeles_lista[i]
    print("III/D:")
    print(f"A legutolsó rendeléshez tartozó email cím: {legutolso_email}")
