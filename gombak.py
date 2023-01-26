import gombak_o


def gombak():
    gombalista = []
    fajl = open("gombak.txt", "r", encoding="utf-8")
    fajl.readline()
    gombaknyersli = fajl.readlines()
    for i in gombaknyersli:
        tiszta = i.strip
        bontott = tiszta.split("@")
        gombalista.append(gombak_o.Gomba(bontott[0], bontott, bontott[2]))
    fajl.close()
    print(gombalista[0].nev)
    #nem tudom mit rontottam el amennyiben megtalálja érdekelne