startHöjd=int(input("Start höjd:"))
höjd=startHöjd
förlust=0.7
while höjd>0.01:
    höjd=höjd*förlust
    studsar=startHöjd/höjd
    studsar=int(studsar)
print(f"Bollen studsar {studsar} gånger")