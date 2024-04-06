
def chislo_na_3(chislo):
    if int(chislo) == 0:
        print("иди нахуй со своим нулем")
        return 0
    if int(chislo) % 3 == 0:
        print("Ахуеть, число делиться на 3")
    else:
        print("Не, нихуя")
def chislo_na_100(chislo):
    if int(chislo) == 0:
        print("иди нахуй со своим нулем")
        return 0
    if int(chislo) % 100 == 0:
        print("Ахуеть, число делиться на 100")
    else:
        print("Не, нихуя")

chislo = input("Введи число: ")
chislo_na_3(chislo)
chislo_na_100(chislo)
