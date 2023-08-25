print("Start to Pet feeder")
menuStr = '========== Menu ==========\n 0.Back to Menu\n 1.Time \n 2.How much? \n 3.Webcam\n 4.Exit\n Select choice :  '
Mainloop = True
while Mainloop:
    choice = input(menuStr)
    if choice == '1': 
        print('== Time ==')
        done = True
        while done:
            numStr = input('Enter your time (1-4) : ')
            if numStr == '0':
                done = False
            elif numStr in ['1','2','3','4'] : 
                num = int(numStr)
                print('You have selected a time of',numStr,'hours.')
                break
            else :
                print("Please enter a valid option 1-4")
           
            
    elif choice == '2' :
        print('== How much? ==')
        done = True
        while done:
            numStr1 = input('How much to feed (10-100g) : ')
            if numStr1 == '0':
                done = False
            elif numStr1 in ['10','20','30','40','50','60','70','80''90','100'] : 
                num = int(numStr1)
                print('You feed the amount',numStr1,'g.')
                break
            else :
                print("Please enter a valid option 0-100g")
        
    elif choice == '3' :
        print('== Webcam ==')
        done = True
        while done:
            numStr1 = input('Do you want to see your Pet? (YES/NO) : ')
            if numStr1 == 'NO':
                done = False
            elif numStr1 == 'YES': 
                c = str(numStr1)
                animal = '''
         /\_/\  
        ( o.o )                      
         > ^ <
        '''             
                  
                print('----system is working----')
                print(animal)
                break
            else :
                print("Please enter a valid option 0-100g")
    elif choice == '4' :
        b = '''
           (__)
           (oo)
     /------\/
    / |    ||
    *  ||----||
       ^^    ^^
'''
        print('====== Exit Program ======')
        print(b)
        Mainloop = False
