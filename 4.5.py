while True:
    n=int(input("n?, Skriv ett tal <=0 för att sluta: "))
    if n <= 0:
        break
    summa = 0
    k=1
    while k<=n:
        summa=summa+k
        k=k+1
    print("Summan blir", summa)

    startHöjd=int(input("Start höjd:"))
höjd=startHöjd
förlust=0.7
while höjd>0.01:
    höjd=höjd*förlust
    studsar=startHöjd/höjd
    studsar=int(studsar)
print(f"Bollen studsar {studsar} gånger")
