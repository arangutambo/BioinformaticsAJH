with open('/Users/antoinejhaddad/Downloads/GC Content Analysis.txt') as Data:
    Input = Data.read()

def DictionarySplitter(DNAUnformatted):
    DNAUnformatted = DNAUnformatted.splitlines()
    DNAStrings = {}
    for line in DNAUnformatted:
        if  line.startswith(">"):
            CurrentID = line[1:]
            DNAStrings[CurrentID] = ""
        else:
            DNAStrings[CurrentID] += line
    return DNAStrings

def GCPercCalculator(DNAString):
    GC = DNAString.count("G") + DNAString.count("C")
    Total = len(DNAString)
    return (GC/Total)*100

def GCMaxIdentifier(DNAStringDictionary):
    GCMaxKey = None
    for Key in DNAStringDictionary.keys():
        if GCMaxKey == None:
            GCMaxKey = Key
        elif GCPercCalculator(DNAStringDictionary[Key]) > GCPercCalculator(DNAStringDictionary[GCMaxKey]):
            GCMaxKey = Key
    return GCMaxKey, GCPercCalculator(DNAStringDictionary[GCMaxKey])
            

DNADict = DictionarySplitter(Input)
GCMaxID, GCMaxValue = GCMaxIdentifier(DNADict)

print(GCMaxID, "\n", GCMaxValue)