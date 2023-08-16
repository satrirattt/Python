score = int(input('Enter score : '))
Grade = ""
print()
if score >= 80 and score <= 100:
    Grade = "A"
elif score >= 70 and score <= 79:
    Grade = "B"
elif score >= 60 and score <= 69:
    Grade = "C"
elif score >= 50 and score <= 59:
    Grade = "D"
elif score >= 0 and score <= 49:
    Grade = "F"
else:
    Grade = ""

if Grade != "":
    print (f"Score value {score}, got grade {Grade}")
else :
    print ("Score not in range.")
