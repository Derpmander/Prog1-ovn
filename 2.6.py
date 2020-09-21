svar=input("Antalet sekunder: ")
sek=int(svar)
tim=sek//3600
sek=sek%3600
min=sek//60#Omvandlar sekund till minut
sek=sek%60#kollar hur många minuter som blir över
print("Timmar: ", tim)
print("Minuter: ", min)
print("Sekunder: ", sek)