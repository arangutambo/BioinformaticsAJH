import pyperclip

InitString = open("/Users/antoinejhaddad/Downloads/DNA Complement Strand.txt", "r")
DNAString = InitString.read()
DNAStringComplement = ""

for x in DNAString:
    if x == "A":
        x = "T"
    elif x == "T":
        x = "A"
    elif x == "G":
        x = "C"
    elif x == "C":
        x = "G"
    DNAStringComplement = x + DNAStringComplement

pyperclip.copy(DNAStringComplement)
InitString.close()
