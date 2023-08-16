print('>> Program Find Maximum Digit <<')
num = int(input('Enter integer number(4 digit) : '))
num1 = num//1000
num2 = (num%1000)//100
num3 = (num%100)//10
num4 = (num%10)//1
Max = 0
if Max < num1:
    Max = num1
if Max < num2:
    Max = num2
if Max < num3:
    Max = num3
if Max < num4:
    Max = num4
    

print(f"Maximum Digit of integer number , {num} = {Max}")
