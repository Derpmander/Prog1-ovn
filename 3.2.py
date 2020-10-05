arskort=float(input("Hur mycket kostar ett årskort: "))
biljett=float(input("Hur mycket kostar en biljett: "))
antal=int(input("Hur många gånger ska du till gymment: "))
x=biljett*antal
if arskort<x:
    print ("Köp ett årskort")
elif arskort>x:
    print ("Köp biljetter om du vill")