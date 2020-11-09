while True:
    startHöjd=int(input("Start höjd:"))#Anger vad start höjden är 
    if startHöjd <= 0:#Händer om det blir ett minus tal
        print("Good job you failed")#Skriver ut en text om det blir ett minus tal
        break #stannar koden
    elif startHöjd >0:#Sker om det blir ett positivt tal
        höjd=startHöjd#Anger höjd som startHöjden
        förlust=0.7#Anger vad som förloras vid varje studs
        while höjd>0.01: #Anger när den ska sluta studsa
            höjd=höjd*förlust #Beräknar höjden
            studsar=startHöjd/höjd #Beräknar antal studsar
            studsar=int(studsar) #Anger studsar
        print(f"Bollen studsar {studsar} gånger") #Skriver ut hur många gånger bollen studsat