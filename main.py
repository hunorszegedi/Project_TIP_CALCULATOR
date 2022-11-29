print("\n\tWELCOME TO THE TIP CALCULATOR\n")
bill = (float)(input("The bill is: "))
people = (int)(input("Split between x people: "))
tip = (int)(input("With tip (x %): "))

amount = "{:.2f}".format((((1 + (tip / 100)) * bill) / people))
print("Each person should pay: " + amount + " dollars.")
