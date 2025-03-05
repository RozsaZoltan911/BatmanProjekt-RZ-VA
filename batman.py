class Batman:
    def __init__(self, nev, szerep, ero):
        self.__nev = nev
        self.setSzerep(szerep)
        self.__ero = ero

    def getNev(self):
        return self.__nev
    
    def setSzerep(self, szerep):
        self.__szerep = szerep

    def getSzerep(self):
        return self.__szerep
    
    def getEro(self):
        return self.__ero

    def __str__(self):
        return f"Neve: {self.getNev()} Szerepe:  {self.getSzerep()} Ereje: {self.getEro()}"
    

karakterek = []
with open('batman.txt', 'r', encoding="utf-8") as fajl:
    for sor in fajl:
        reszek = sor.strip().split()
        nev = reszek[0]
        szerep = reszek[1]
        ero = int(reszek[2])
        karakterek.append(Batman(nev, szerep, ero))


db=6
while len(karakterek) < db:

    van_nev = False
    while not van_nev:
        nev = input("Add meg a karakter nevét: ")
        van_nev = True  
        for k in karakterek:
            if k.getNev() == nev:  
                print("Ez a karakter már benne van a listában!")
                van_nev = False  
                db+=1


    van_szerep = False
    while not van_szerep:
        szerep = input("Add meg a karakter szerepét(hős, gonosztevő, mellékszereplő): ").strip().lower()
        if szerep == "hős" or szerep =="gonosztevő" or szerep =="mellékszereplő":
            van_szerep = True
        else:
            print("Helytelen szerep!")
            
    end = False
    while not end:
        ero = int(input("Add meg a karakter erejét: "))
        if 0<=ero<=100:
            end=True
        else:
            print("Helytelen erő érték!")

    karakterek.append(Batman(nev, szerep, ero))

    for k in karakterek:
        print("\t",k)


def Legerosebb(karakterek):
    legerosebb = karakterek[0]
    for k in karakterek:
        if k.getEro() > legerosebb.getEro():
            legerosebb = k
    return f"A legerosebb karakter: {k.getNev()}\nEro: {k.getEro()}"

with open('legerosebb.txt', 'a', encoding="utf-8") as fajl:
    fajl.write(Legerosebb(karakterek))

def Szerepek(karakterek):
    hos = 0
    gonosz = 0
    mellek = 0

    for k in karakterek:
        if k.getSzerep() == "hős":
            hos += 1
        elif k.getSzerep() == "gonosztevő":
            gonosz += 1
        else:
            mellek += 1  

    if hos >= gonosz and hos >= mellek:
        legtobb_szerep = "hős"
    elif gonosz >= hos and gonosz >= mellek:
        legtobb_szerep = "gonosztevő"
    else:
        legtobb_szerep = "mellékszereplő"

    print(f"\nA legtöbb karakter'{legtobb_szerep}' szerepű .\n")


    szurt_karakterek = []
    for k in karakterek:
        if k.getSzerep() == legtobb_szerep:
            szurt_karakterek.append(k)



    