class Karakter:
    def __init__(self, nev, szerep, power):
        self.__nev = nev
        self.__szerep = szerep
        self.__power = power
    
    def getNev(self):
        return self.__nev
    
    def getSzerep(self):
        return self.__szerep
    
    def getPower(self):
        return self.__power
    
    def __str__(self):
        return f"{self.getNev()} | {self.getSzerep()} | {self.getPower()}"

    def write_to_file(self):
        with open('batman.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(f"{self.getNev()} {self.getSzerep()} {self.getPower()}\n")

def fajlhozFuzes(mentendoKarakter):
    with open("batman.txt", "a", encoding="utf-8") as fajl:
        print(mentendoKarakter.getNev(), mentendoKarakter.getSzerep(), mentendoKarakter.getPower(),file=fajl)



karakterek=[]
with open('batman.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adat = sor.strip().split(" ")
        karakter = Karakter(adat[0], adat[1], adat[2])
        karakterek.append(karakter)


for karakter in karakterek:
    print(karakter)

tartozKarakterrel = 3


while tartozKarakterrel>0:
    print("Megadandó karakterek száma: ", tartozKarakterrel)
    nev = input("Adjon meg egy nevet! ")
    szerepel = False
    for karakter in karakterek:
        if karakter.getNev().lower()==nev.lower():
                szerepel = True
    if szerepel:
                print("Ez már szerepel! ")
                tartozKarakterrel += 1
    else:
        ero = int(input("Add meg a karakter erejét! "))
        szerep = input("Add meg a karakter szerepét! ")
        mentendoKarakter = Karakter(nev, szerep, ero)
        karakterek.append(mentendoKarakter)
        tartozKarakterrel -= 1
        fajlhozFuzes(mentendoKarakter)

with open("legerosebb.txt", "w", encoding="utf-8") as fajl:
    legerosebb = karakterek[0]
    for eromero in karakterek:
        if int(eromero.getPower())>int(legerosebb.getPower()):
            legerosebb = eromero
    print(f"{legerosebb.getNev()}, {legerosebb.getSzerep()},{legerosebb.getPower()}", file=fajl)
print("A legerősebb karakter: \n", legerosebb)


class Szerep:
    def __init__(self,sznev,szama):
        self.__sznev = sznev
        self.__szama = szama
    
    def getSznev(self):
        return self.__sznev
    def getSzama(self):
        return self.__szama
    def setSzama(self,szama):
        self.__szama = szama

    def __str__(self):
         return f"Szerep: {self.getSznev()}, száma: {self.getSzama()}"
    
sz1 = Szerep("Hős", 0)
sz2 = Szerep("Gonosztevő", 0)
sz3 = Szerep("Mellékszereplő", 0)
szerepek = [sz1,sz2,sz3]

for x in karakterek:
    if x.getSzerep().lower()==sz1.getSznev().lower():
        sz1.setSzama(sz1.getSzama()+1)
    elif x.getSzerep().lower()==sz2.getSznev().lower():
        sz2.setSzama(sz2.getSzama()+1)
    else:
        sz3.setSzama(sz3.getSzama()+1)
for szerep in szerepek:
    print(szerep)

legtobbszerep=szerepek[0]
for szerep in szerepek:
    if int(legtobbszerep.getSzama())<int(szerep.getSzama()):
        legtobbszerep = szerep
        
for karakter in karakterek:
    if karakter.getSzerep().lower()==legtobbszerep.getSznev().lower():
        print(karakter)