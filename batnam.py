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

vege = False
van_nev = False
van_szerep = False
end=False
db=6
while len(karakterek) != db:

    while not van_nev:
        nev = input("Add meg a karakter nevét: ")
        for k in karakterek:
            if k.getNev() == nev:
                db+=1  
                print("Ez a karakter már benne van a listában!")
            else:
                van_nev = True
    while not van_szerep:
        szerep = input("Add meg a karakter szerepét(hős, gonosztevő, mellékszereplő): ").strip().lower()
        if szerep == "hős" or szerep =="gonosztevő" or szerep =="mellékszereplő":
            van_szerep = True
        else:
            print("Helytelen szerep!")
            
    while not end:
        ero = int(input("Add meg a karakter erejét: "))
        if 0<=ero<=100:
            karakterek.append(Batman(nev, szerep, ero))
            end=True
        else:
            print("Helytelen erő érték!")
    for k in karakterek:
        print("\t",k)
    van_nev = False
    van_szerep = False
    end=False
def Legerosebb(karakterek):
    legerosebb = karakterek[0]
    for k in karakterek:
        if k.getEro() > legerosebb.getEro():
            legerosebb = k
    return f"A legerosebb karakter: {k.getNev()}\nEro: {k.getEro()}"

with open('legerosebb.txt', 'a', encoding="utf-8") as fajl:
    fajl.write(Legerosebb(karakterek))
    
