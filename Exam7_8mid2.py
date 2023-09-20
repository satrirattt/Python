#Program name : Exam7_8.py
from random import randint

def genData(std,sub):
    scores = []
    for r in range(student):
        scores.append([]) #add list
        for c in range(subject):
            scores[r].append(randint(0,100)) #random value
    return scores

def displayData(scores):
    n = 1
    for score in scores:
        print(f"|Std %2d "%n,end='')
        for s in score:
            print(f"| %3s "%s,end='')
        print("|",end='')
        print(sum(score)/subject,end='')
        print("|",end='')
        print(max(score),end='')
        print("|",end='')
        print(min(score),end='')
        print("|")
        n = n + 1
        
#main program
student = int(input("Enter number of student : "))
subject = int(input("Enter number of subject : "))

#create ;ist variable
Scores = genData(student,subject)

#generate data in list
displayData(Scores);
