def bilet(nom):
    polovina1 = 0
    polovina2 = 0
    for i in nom[0:int(len(nom)/2)]:
        polovina1 += int(i)
    for i in nom[int(len(nom)/2):len(nom)]:
        polovina2 += int(i)
    if polovina1 == polovina2:
        print("О, счастливый, класс")
    else:
        print("Несчастливый, лох")

nom= input("Номер введи: ")
bilet(nom)