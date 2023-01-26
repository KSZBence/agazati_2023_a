def elso_idos(lista):
        for i in range(len(lista)):
            if lista[i] > 70:
                return i

        return -1


def konzolra_ir(szoveg):
    print("Első idős ember korának helye a listában:", szoveg)


def fajl_ir(szoveg):
    fajl = open("oreg.txt", "w", encoding="utf-8")
    print(f"II/F:\n\tElső idős ember korának helye a listában: {szoveg}", file=fajl)
    fajl.close()


def korok():
    korlista = []
    for i in range(5):
        korlista.append(int(input("Adj meg egy egész számot: ")))

    print("II/A, B, C:\n\t", end="")
    for i in range(len(korlista)):
        if i == len(korlista)-1:
            print(korlista[i])
        else:
            print(korlista[i],end=":")

    print("II/D, E:\n\t", end="")
    konzolra_ir(elso_idos(korlista))
    fajl_ir(elso_idos(korlista))


