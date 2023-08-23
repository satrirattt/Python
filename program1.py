menuStr = 'Main Menu\n----------\n 1.Exercise 1\n 2.Exercise 2\n'
menuStr += ' 3.Exercise 3\n 4.Exit\nSelect choice : '
Mainloop = True
while Mainloop:
    choice = input(menuStr)
    if choice == '1':
        print('>> Program Fing Maximum Digit <<')
        done = True
        
        while done:
            numStr = input('Enter integer number(0-exit) : ')
            if numStr == '0':
                done = False
            else : #find max
                Max = 0
                #1(String) for n in range(len(numStr)):
                #    digitStr = numStr[n]
                #2(String) for digitStr in numStr:
                #   digit = int(digitStr)
                #   if digit > Max:
                #       Max = digit
                #>>int
                num = int(numStr)
                while num > 0:
                    digit = num % 10
                    num = num // 10
                    if digit > Max :
                        Max = digit
                print(f'Maximum digit of integer {numStr} = {Max}')
        print('Exit Program')
    elif choice == '2' :
        pass
    elif choice == '3' :
        pass
    elif choice == '4' :
        Mainloop = False
