import pyperclip

DataSet = open("/Users/antoinejhaddad/Downloads/Mendel's First Law.txt", "r")
DataSetRead = DataSet.read()
OrganismAmounts = DataSetRead.split(" ")

k = int(OrganismAmounts[0])
m = int(OrganismAmounts[1])
n = int(OrganismAmounts[2])

N = k + m + n

ProbabilityDominant = (1/(N*(N-1)))*(k*((k-1)+m+n)+m*(k+(m-1)*0.75+n*0.5)+n*(k + m*0.5))

pyperclip.copy(ProbabilityDominant)

DataSet.close()



