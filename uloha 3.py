x= float(input("zadaj minimalnu hodnotu intervalu"))
y= float(input("zadaj maximalnu hodnotu intervalu"))
c= float(input("zadaj cislo"))
if c<=x:
    print("cislo nepatri do intervalu moc male")
elif c>=y:
    print("cislo nepatri do intervalu moc velke")
else:
    print("cislo patri do intervalu")