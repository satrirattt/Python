num = int(input('Enter number : '))
Max = 0
'''
for n in range(4):
    digit = num % 10
    if Max < digit:
        Max = digit
    num = num // 10
'''
#1
digit = num % 10
if Max < digit:
    Max = digit
num = num //10
#2
digit = num % 10
if Max < digit:
    Max = digit
num = num //10
#3
digit = num % 10
if Max < digit:
    Max = digit
num = num //10
#4
digit = num % 10
if Max < digit:
    Max = digit
num = num //10
print(f"Maximum number : {Max}")

