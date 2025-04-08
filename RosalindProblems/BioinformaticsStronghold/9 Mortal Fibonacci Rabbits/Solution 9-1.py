import pyperclip

with open() as Data:
    RabbitsData = Data.read()
    RabbitsData = RabbitsData.split(" ")

n = int(RabbitsData[0])
m = int(RabbitsData[1])

def RabbitPopulation(month):
    if month == 1 or month == 2:
        return 1
    else:
        return RabbitPopulation(month - 1) -  RabbitPopulation(month - 2)

pyperclip.copy(RabbitPopulation(n))