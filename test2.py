print(45 * '-')
print('| Program Calculate Grade Point Average |'.center(45))
print(45 * '-')
print('Input Data:')

for n in enumerate (0,5):
    n1 = input(f'Enter subject name({n + 1}) : ')
    score = float(input(f'Enter subject score({n+1}) : '))
    print()

def grade(score) :
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60 :
        return 'C'
    elif score >= 50 :
        return 'D'
    else :
        return 'F'

g_point = {
    'A' : 4.0,
    'B' : 3.0,
    'C' : 2.0,
    'D' : 1.0,
    'F' : 0.0,
    }

print(' Grade Point Average(GPA) Report '.center(45))
print(45 * '-')
print('No. Subject Name        Mark Grade Points'.center(45))
print(45 * '-')
