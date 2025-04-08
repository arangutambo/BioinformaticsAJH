import pyperclip

with open('/Users/antoinejhaddad/Downloads/Expected Offspring Calculation.txt') as Data:
    Offspring = Data.read()

Offspring = Offspring.split(" ")

def ChanceDominantTrait(Populations):
    Chance = (float(Populations[0])+float(Populations[1])+float(Populations[2])+float(Populations[3])*3/4+float(Populations[4])*1/2)
    return Chance

pyperclip.copy(ChanceDominantTrait(Offspring)*2)