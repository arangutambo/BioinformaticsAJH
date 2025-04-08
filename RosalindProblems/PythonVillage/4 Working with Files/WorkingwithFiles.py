DataSet = open("/Users/antoinejhaddad/Downloads/Rosalind Working with Files.txt", "r")
Lines = DataSet.readlines()
Document = open("EvenLines.txt", "a")

for line in Lines:
    a = Lines.index(line)
    if a % 2 == 1:
        Document.write(line + "\n")
