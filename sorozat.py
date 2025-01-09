import random

def feladat2():
    print("II/A, B, C:")
    randomszamok = []
    i:int = 1
    while i <= 5:
        szam1:int = random.randint(1,10)
        randomszamok.append(szam1)
        if i == 5:
            print(f"{szam1}")
        else:
            print(f"{szam1}", end="!")
        i += 1
    return randomszamok

def nagyobb(randomszamok):
    szamlalo:int=0
    for i in range(0, len(randomszamok), 1):
        if randomszamok[i] > randomszamok[i-1]:
            szamlalo += 1
    return szamlalo

def konzol_ir(szamlalo):
    print("II/D, E:")
    print(f"Nagyobb számok száma: {szamlalo}.")

def fajba_ir(szamlalo):
    file = open("vegeredmeny.txt", 'w', encoding='UTF-8')
    file.write("II/F:\n")
    file.write(f"Nagyobb számok száma: {szamlalo}.")
    file.close()

