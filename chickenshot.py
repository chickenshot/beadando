from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=5000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                print("A szoba már foglalt ezen a napon.")
                return
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                print("Foglalás sikeres.")
                return
        print("Nincs ilyen szoba a szállodában.")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Lemondás sikeres.")
                return
        print("Nincs ilyen foglalás.")

    def listaz(self):
        print("Foglalások:")
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# Szálloda, szobák és foglalások inicializálása
szalloda = Szalloda("Hotel XYZ")
szalloda.add_szoba(EgyagyasSzoba("101"))
szalloda.add_szoba(EgyagyasSzoba("102"))
szalloda.add_szoba(KetagyasSzoba("201"))
szalloda.add_szoba(KetagyasSzoba("202"))
szalloda.add_szoba(KetagyasSzoba("203"))

foglalasok_kezelo = FoglalasKezelo(szalloda)
foglalasok_kezelo.foglalas("101", datetime(2024, 5, 10))
foglalasok_kezelo.foglalas("202", datetime(2024, 5, 12))
foglalasok_kezelo.foglalas("101", datetime(2024, 5, 15))
foglalasok_kezelo.foglalas("203", datetime(2024, 5, 18))
foglalasok_kezelo.foglalas("102", datetime(2024, 5, 20))

# Felhasználói interfész és adatvalidáció
while True:
    print("\nVálassz műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("0. Kilépés")

    valasztas = input("Választott művelet: ")

    if valasztas == "1":
        szobaszam = input("Add meg a szoba számát: ")
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("A dátumnak a jövőben kell lennie.")
            else:
                foglalasok_kezelo.foglalas(szobaszam, datum)
        except ValueError:
            print("Hibás dátum formátum.")
    elif valasztas == "2":
        szobaszam = input("Add meg a szoba számát: ")
        datum = input("Add meg a lemondás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            foglalasok_kezelo.lemondas(szobaszam, datum)
        except ValueError:
            print("Hibás dátum formátum.")
    elif valasztas == "3":
        foglalasok_kezelo.listaz()
    elif valasztas == "0":
        break
    else:
        print("Érvénytelen választás.")
