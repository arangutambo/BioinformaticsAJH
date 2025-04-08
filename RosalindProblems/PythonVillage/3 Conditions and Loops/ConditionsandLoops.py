a = 4984
b = 8992

SumOddAB = 0
num = a

while num >= a and num <= b:
    if num % 2 == 1:
        SumOddAB = SumOddAB + num
    num = num + 1

print(SumOddAB)