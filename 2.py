def magia_na(data):
    if int(data[8]+data[9]) == int(data[0]+data[1])*int(data[3]+data[4]):
        print("О, волшебная, крута")
    else:
        print("Только очко у тебя волшебное,а дата нет")


data= input("Дату введи: ")
magia_na(data)