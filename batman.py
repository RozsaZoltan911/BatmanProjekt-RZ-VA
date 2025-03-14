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
        return self.__szerep.capitalize()
    
    def getEro(self):
        return self.__ero

    def __str__(self):
        return f"Neve: {self.getNev()} Szerepe:  {self.getSzerep()} Ereje: {self.getEro()}"
    

karakterek = []
with open('batman.txt', 'r', encoding="utf-8") as fajl:
    for sor in fajl:
        reszek = sor.strip().split()
        if len(reszek) == 3:  
            nev = reszek[0]
            szerep = reszek[1]
            try:
                ero = int(reszek[2])
                karakterek.append(Batman(nev, szerep, ero))
            except ValueError:
                print(f"Hibás erő érték: {reszek[2]}")  


def Fuzes(uj_karakter):
    existing_names = []
    
    with open('batman.txt', 'r', encoding="utf-8") as fajl:
        for sor in fajl:
            reszek = sor.strip().split()
            if len(reszek) >= 1: 
                existing_names.append(reszek[0])  
    
    if uj_karakter.getNev() not in existing_names:  
        with open('batman.txt', 'a', encoding="utf-8") as fajl:
            fajl.write(f"{uj_karakter.getNev()} {uj_karakter.getSzerep()} {uj_karakter.getEro()}\n")
    else:
        print(f"A {uj_karakter.getNev()} karakter már létezik a fájlban!")

db = 6
while len(karakterek) < db:
    van_nev = False
    while not van_nev:
        nev = input("Add meg a karakter nevét: ")
        van_nev = True  
        for k in karakterek:
            if k.getNev() == nev:  
                print("Ez a karakter már benne van a listában!")
                van_nev = False  
                db += 1  

    van_szerep = False
    while not van_szerep:
        szerep = input("Add meg a karakter szerepét(hős, gonosztevő, mellékszereplő): ").strip().lower()
        if szerep in ["hős", "gonosztevő", "mellékszereplő"]:
            van_szerep = True
        else:
            print("Helytelen szerep!")
            
    end = False
    while not end:
        try:
            ero = int(input("Add meg a karakter erejét (0-100): "))
            if 0 <= ero <= 100:
                end = True
            else:
                print("Helytelen erő érték!")
        except ValueError:
            print("Hibás bemenet! Számot adj meg.")

    uj_karakter = Batman(nev, szerep, ero)
    karakterek.append(uj_karakter)

    Fuzes(uj_karakter)  

    for k in karakterek:
        print("\t", k, ";")

    if db - len(karakterek) > 0:
        print(f"Még kell {db - len(karakterek)} db karakter")


def Legerosebb(karakterek):
    legerosebb = karakterek[0]
    for k in karakterek:
        if k.getEro() > legerosebb.getEro():
            legerosebb = k
    return f"A legerosebb karakter: {legerosebb.getNev()}\nEro: {legerosebb.getEro()}"

with open('legerosebb.txt', 'w', encoding="utf-8") as fajl:  
    fajl.write(Legerosebb(karakterek))


def Szerepek(karakterek):
    roles_count = {"hős": 0, "gonosztevő": 0, "mellékszereplő": 0}

    for k in karakterek:
        roles_count[k.getSzerep().lower()] += 1

    max_count = max(roles_count.values())
    max_roles = []
    for role, count in roles_count.items():
        if count == max_count:
            max_roles.append(role)
    
    legtobb_szerep = "/".join(max_roles)
    if len(max_roles) > 1:
        legtobb_szerep += " (döntetlen)"

    print(f"\nA legtöbb karakter '{legtobb_szerep}' szerepű.\n")
    print(f"\tA {legtobb_szerep} szerepű karakterek ereje csökkenő sorrendben:")
    
    szurt_karakterek = []
    for k in karakterek:
        if k.getSzerep().lower() in max_roles:
            szurt_karakterek.append(k)
    
    szurt_karakterek.sort(key=lambda k: int(k.getEro()), reverse=True)
    # for i in range(len(szurt_karakterek) - 1):
    #     for j in range(i + 1, len(szurt_karakterek)):
    #         if szurt_karakterek[i].getEro() < szurt_karakterek[j].getEro():
    #             szurt_karakterek[i], szurt_karakterek[j] = szurt_karakterek[j], szurt_karakterek[i]
    
    for k in szurt_karakterek:
        print("\t", k, ";")

Szerepek(karakterek)
