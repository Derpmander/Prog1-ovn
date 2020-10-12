vaken=input("Have you awoken?")

if vaken=="yes":
    print("Good job")
    ready=input("Are you ready?")
    if ready=="yes":
        print("Good job")
    elif ready=="mabye":
        print("Don't go playing games")
    elif ready=="no":
        print("Well get ready then")
elif vaken=="no":
    print("WAKE UP")
    woke=input("HAVE YOU AWOKEN")
    if woke=="yes":
        print("Good job")
    elif woke=="no":
        print("Since you answered get your butt moving")
else:
    print("😴")