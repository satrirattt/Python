numStr = tol = q = 0
n = 1
menu1 = []
menu2 = []
menu3 = []
menu4 = []


orders =[]

Mainloop = True
while Mainloop:
    print(24 * '=')
    print('|     Drinks Menu      |'.center(20))
    print(24 * '=')
    menu =  '| 0. Quit              |\n'.center(21)
    menu += '| 1. Hot Coffee        |\n'.center(20)
    menu += '| 2. Ice Coffee        |\n'.center(20)
    menu += '| 3. Frappe Coffee     |\n'.center(20)
    menu += '| 4. Calculate Cost    |\n'.center(20)
    menu += '========================\n'.center(20)
    menu += 'Select Item :  '
    choice = input(menu)
    if choice == '0' :
        print('====== Exit Program ======')
        Mainloop = False
        
    if choice == '1': 
        done = True
        while done:
            numStr = int(input('Hot Coffee, how many glasses : '))
            name = "Hot Coffee"
            prc = 35.00
            To = numStr*prc
            q = q+1
            menu1.append(numStr)
            menu2.append(name)
            menu3.append(prc)
            menu4.append(To)
            break
        
    elif choice == '2' :
        done = True
        while done:
            numStr = int(input('Ice Coffee, how many glasses : '))
            name = "Ice Coffee"
            prc = 50.00
            To = numStr*prc
            q = q+1
            menu1.append(numStr)
            menu2.append(name)
            menu3.append(prc)
            menu4.append(To)
            break
        
    elif choice == '3' :
        done = True
        while done:
            numStr = int(input('Frappe Coffee, how many glasses : '))
            name = "Frappe Coffee"
            prc = 60.00
            To = numStr*prc
            q = q+1
            menu1.append(numStr)
            menu2.append(name)
            menu3.append(prc)
            menu4.append(To)
            break
        
    elif choice == '4' :
        print(f"""Order #{n}: 
----------------------------------- 
Qty Item          Price   Total 
-----------------------------------""")
        n+=1
        for i in range (0,q):
            print(f"{menu1[i]}   {menu2[i]}    {menu3[i]:.2f}   {menu4[i]:.2f}")
            tol = menu4[i] + tol
        print(f"""-----------------------------------
Total: {tol} Bath""")
        menu1.clear()
        menu2.clear()
        menu3.clear()
        menu4.clear()
        q=0
        tol=0
                  
