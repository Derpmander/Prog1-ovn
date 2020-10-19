from fractions import Fraction as Fraction
n=float(input("n?"))
summa=0
k=1
while k<=Fraction(1,n):
    summa=summa+k
    k=k+1
print(Fraction(1,k))