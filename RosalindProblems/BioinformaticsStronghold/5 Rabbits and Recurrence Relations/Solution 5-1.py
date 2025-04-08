import pyperclip

DataSet = open("/Users/antoinejhaddad/Downloads/Rabbits and Recurrence Relations.txt", "r")
DataSetRead = DataSet.read()
RabbitsAndTime = DataSetRead.split(" ")

n = 5
# int(RabbitsAndTime[0])
k = 3
# int(RabbitsAndTime[1])
TotalPairs = 1
month = 0

while month <= n:
    TotalPairs = TotalPairs + TotalPairs*k
    month = month + 1


pyperclip.copy(TotalPairs)

DataSet.close()



