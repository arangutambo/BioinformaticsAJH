with open("/Users/antoinejhaddad/Downloads/Rabbits and Recurrence Relations (2).txt") as Data:
    RabbitsData = Data.read()
    RabbitsData = RabbitsData.split(" ")

n = int(RabbitsData[0])
k = int(RabbitsData[1])

def RabbitsPerM(month):
    if month == 1 or month == 2:
        return 1
    else:
        return RabbitsPerM(month - 1) + k * RabbitsPerM(month - 2)

print(RabbitsPerM(n))


