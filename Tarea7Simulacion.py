import random as rad
from time import sleep


class Person:
    def __init__(self, num, weight, floor):
        self.num = num
        self.weight = weight
        self.floor = floor


listLobby = []
listLobbyba = []
list1 = []
list1ba = []
list2 = []
list2ba = []
list3 = []
list3ba = []


for i in range(1, 11):
    listLobby.append(Person(i, rad.randint(70, 350), rad.randint(0, 3)))

for i in range(11, 14):
    list1.append(Person(i, rad.randint(70, 350), rad.randint(0, 3)))

for i in range(14, 17):
    list2.append(Person(i, rad.randint(70, 350), rad.randint(0, 3)))

for i in range(17, 20):
    list3.append(Person(i, rad.randint(70, 350), rad.randint(0, 3)))

a = 5
elevator = []

maxWeight = int(input("Peso que puede soportar el ascensor(en libras): "))

countWeight = 0
maxP = int(input("Maximo de personas que pueden entrar: "))
countElevator = 0
countFloor = 0
totalElevator = 0
count = 0
while count < 19:
    # las personas que se quedaran en el lobby y personas entrando al elevador
    for i in reversed(elevator):
        if i.floor == 0:
            listLobbyba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight

    for i in reversed(listLobby):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(listLobby.pop(listLobby.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Lobby")
    print("Cantidad de personas que se quedaron en el lobby:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador en el lobby: " + str(countElevator))
    print("Total de personas dentro del elevador al momento: " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0

    # personas saliendo al piso 1
    for i in reversed(elevator):
        if i.floor == 1:
            list1ba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight

    # personas que estaban en el piso 1 entrando al elevador
    for i in reversed(list1):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(list1.pop(list1.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Segundo piso")
    print("Cantidad de personas que se quedaron en el segundo piso:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador en el segundo piso: " + str(countElevator))
    print("Total de personas dentro del elevador al momento: " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0

    # personas saliendo del elevador al piso 2
    for i in reversed(elevator):
        if i.floor == 2:
            list2ba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight

    # personas del piso 2 entrando al elevador
    for i in reversed(list2):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(list2.pop(list2.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Tercer piso")
    print("Cantidad de personas que se quedaron en el tercer piso:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador en el tercer piso:" + " " + str(countElevator))
    print("Total de personas dentro del elevador al momento:" + " " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0

    # personas del saliendo del elevador al piso 3
    for i in reversed(elevator):
        if i.floor == 3:
            list3ba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight

    # personas del piso 3 entrando al elevador
    for i in reversed(list3):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(list3.pop(list3.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Cuarto piso")
    print("Cantidad de personas que se quedaron en el cuarto piso:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador en el cuarto piso:" + " " + str(countElevator))
    print("Total de personas dentro del elevador al momento:" + " " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0

    # Elevador bajando del piso 3 al piso 2
    for i in reversed(elevator):
        if i.floor == 2:
            list2ba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight

    # personas del piso 2 entrando al elevador
    for i in reversed(list2):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(list2.pop(list2.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Tercer piso")
    print("Cantidad de personas que se quedaron en el tercer piso:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador en el tercer piso:" + " " + str(countElevator))
    print("Total de personas dentro del elevador al momento:" + " " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0

    # elevador bajando del piso 2 al 1
    for i in reversed(elevator):
        if i.floor == 1:
            list1ba.append(elevator.pop(elevator.index(i)))
            count += 1
            countFloor += 1
            countWeight -= i.weight
    if count == 19:
        break

    for i in reversed(list1):
        if countElevator < maxP and countWeight < maxWeight and countWeight + i.weight <= maxWeight:
            elevator.append(list1.pop(list1.index(i)))
            countElevator += 1
            totalElevator += 1
            countWeight += i.weight

    print("Segundo piso")
    print("Cantidad de personas que se quedaron en el segundo piso:" + " " + str(countFloor))
    print("Cantidad de personas que subieron al elevador segundo piso: " + str(countElevator))
    print("Total de personas dentro del elevador al momento: " + str(len(elevator)))
    print("Peso total en el elevador: " + str(countWeight))
    print("Total de personas que se han quedado en su piso deseado(total debe ser 19)" + str(count))
    sleep(a)
    print("--------------------")
    if count == 19:
        break
    countFloor = 0
    countElevator = 0


print("--------------------")
print("RESULTADOS")
print("PERSONAS EN EL LOBBY")
for i in listLobbyba:
    print("Numero#: ", i.num, " Peso: ", i.weight)
print("-------")
print("PERSONAS EN EL SEGUNDO PISO")
for i in list1ba:
    print("Numero#: ", i.num, " Peso: ", i.weight)
print("--------")
print("PERSONAS EN EL TERCER PISO")
for i in list2ba:
    print("Numero#: ", i.num, " Peso: ", i.weight)
print("--------")
print("PERSONAS EN EL CUARTO PISO")
for i in list3ba:
    print("Numero#: ", i.num, " Peso: ", i.weight)
