a = int(input("Enter amount  : "))

b = float(input("Enter rate : "))/100

c = int(input("Enter year : " ))

Fv = a * ( 1 + b ) ** c
print("Future value = ", Fv)

