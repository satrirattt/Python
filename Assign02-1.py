ATM = int(input("Enter number money withdraw : "))
print()

c1 = int(ATM)//1000
print("Cash B1000 : ", float(c1))
c2 = int(ATM%1000)//500
print("Cash B500 : ", float(c2))
c3 = int(ATM%500)//100
print("Cash B100 : ", float(c3))

