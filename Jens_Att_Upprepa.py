import random
gissa=0
försök=0
correct= random.randint(1,3)
while gissa !=correct:
    försök+=1
    gissa=int(input("Skriv din gissning, Helst ett hel tal: "))
    if gissa <correct:
        print("för litet")
    elif gissa >correct:
        print("för stort")
else:
    print("Rätt")
print (f"Antal försök: {försök}")
print (f"The number was {correct}")
