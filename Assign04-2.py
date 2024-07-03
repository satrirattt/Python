print(45 * '=')
print('| Program Calculate Grade Point Average |'.center(45))
print(45 * '=')
print('Input Data:')

sub = []
sc = []
tol = 0

for n in range (0,5):
    n1 = input(f'Enter subject name({n + 1}) : ')
    score = float(input(f'Enter subject score({n+1}) : '))
    sub.append(n1)
    sc.append(score)
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
    'A' : 4.0*3,
    'B' : 3.0*3,
    'C' : 2.0*3,
    'D' : 1.0*3,
    'F' : 0.0,
    }

print(' Grade Point Average(GPA) Report '.center(45))
print(45 * '=')
print('No. Subject Name        Mark Grade    Points'.center(45))
print(45 * '=')

for n in range (0,5):
    subname = sub[n]
    scname = sc[n]
    grade_sc = grade(scname)
    grade_points = g_point.get(grade_sc, 0)
    print(f'{n + 1 :>3} {subname:<22} {scname:<5.1f} {grade_sc:<8}{grade_points:.1f}')
    tol = grade_points + tol
print(f"""=============================================
Total Points : {tol}
Total Credits : 15.0
Grade Point Average(GPA) : {tol/15:.2f}""")



