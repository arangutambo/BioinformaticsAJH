with open("/Users/antoinejhaddad/Downloads/Rosalind Dictionaries.txt", "r") as DataSet:
    s = DataSet.read()

Words = s.split(" ")

WordAmounts = {}

for x in Words:
    if x not in WordAmounts:
        WordAmounts[x] = 1
    elif x in WordAmounts:
        WordAmounts[x] = WordAmounts[x] + 1

# print(WordAmounts)

for key in WordAmounts:
    print(key + " " + str(WordAmounts[key]))