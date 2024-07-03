while True:
    num = int(input('Enter number(2-12) : '))

    if num == 0:
        break

    if num < 2 or num > 12:
        continue

    print(65 * '-')
    print('Multplication Table'.center(65))
    print(65 * '-')
        

    for i in range(1,13):
        for n in range(num, num + 4):
            print(f'{n} * {i} = {n * i}\t|',end='')
        print()
        
    
