class Gitare():
    def __init__(self, brend, tip):
        self.brend = brend
        self.tip = tip

    def __str__(self):
        return f"Objekat klase Gitare, brend={self.brend}, tip={self.tip}"

g1 = Gitare(brend="gibson", tip="elektricna")
g2 = Gitare(brend="fender", tip="akusticna")
g3 = Gitare(brend="gibson", tip="akusticna")

print(g3.brend, g3.tip)
print(g1)

class Osnovna:
    atr_klase = "Iz klase Osnovna"

class Izvedena(Osnovna):
    atr_izvedene = "Iz klase Izvedena"

i1 = Izvedena()

print(i1.atr_klase)
print(i1.atr_izvedene)

# Inheritance with __init__
# Bazna klasa (parent)
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called for {self.name}")

    def speak(self):
        print("Animal makes a sound")


# Izvedena klasa (child)
class Dog(Animal):
    def __init__(self, name, breed):
        # Pozivamo __init__ iz parent klase
        super().__init__(name)
        self.breed = breed
        print(f"Dog __init__ called for {self.name}, breed: {self.breed}")

    def speak(self):
        print(f"{self.name} says: Woof!")


d = Dog("Rex", "Labrador")
d.speak()