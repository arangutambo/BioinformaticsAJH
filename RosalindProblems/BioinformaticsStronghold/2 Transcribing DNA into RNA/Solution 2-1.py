import pyperclip

Strand = open("/Users/antoinejhaddad/Downloads/Transcribing DNA to RNA.txt", "r")
DNAStrand = Strand.read()

RNAStrand = DNAStrand.replace("T", "U")
pyperclip.copy(RNAStrand)

Strand.close()