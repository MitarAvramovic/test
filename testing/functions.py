def saberi(a, b):
    return a + b


def oduzmi(a, b):
    return a - b


def pomnozi(a, b):
    return a * b


def podeli(a, b):
    if b == 0:
        return "Deljenje sa nulom nije dozvoljeno"
    return a / b


print(saberi(100, 200))
print(oduzmi(200, 100))
print(pomnozi(2, 2))
print(podeli(9, 0))


def obrni(l):
    return l[::-1]


l1 = [1, 2, 3]

print(obrni(l1))
