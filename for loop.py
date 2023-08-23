num = int(input('Enter line number : '))
typed = input('Enter type (1-4) : ')
if typed == '1' :
    for r in range(1, num+1):
        for c in range(1,r+1):
            print('#',end='')
        print()
elif typed == '2' :
    for r in range(1, num+1):
        for c in range(1,num+2-r):
            print('#',end='')
        print()
elif typed == '3' :
    for r in range(1, num+1):
        for c in range(1,num+1):
            if c >= r :
                print('#',end='')
            else :
                print(' ',end='')
        print()
elif typed == '4' :
    #for r in range(1, num+1):
    #   for c in range(1,num+1):
    #      if c  > num - r :
    #         print('#',end='')
    #    else :
    #       print(' ',end='')
          
    #print()
    r = 1
    while r <= num :
        c = 1
        while c <= num :
            print('#',end='') if c > num -r else print(' ',end= '')
                #if c > num - r :
                #    print('#',end='')
                #else :
                #   print(' ',end='')
            c += 1
        print()
        r += 1
    
            
