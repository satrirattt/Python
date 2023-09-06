import math
def select_menu():
    print("Menu")
    print("1. circle 2. rectangle")
    print("3. triangle 4. Exit")
    menu = input("please choose : ")
    return(menu)

def cal_circle(radius):
    area = math.pi*radius*radius
    return(area)

def cal_rectangle(width,height):
    area = width * height
    return(area)

def cal_triangle(base,high):
    area = 0.5 * base * high
    return(area)

def main():
    done = True
    while done:
        print()
        print("Program calculate area.")
        menu = select_menu()
        if menu == "1":
            radius = int(input("Enter radius : "))
            print("Area of circle = ",cal_circle(radius))
        elif menu == "2": 
            width = int(input("Enter width : "))
            height = int(input("Enter height : "))
            print("Area of rectangle = ", cal_rectangle(width,height))
        elif menu == "3":
            base = int(input("Enter base : "))
            high = int(input("Enter high : "))
            print("Area of triangle = ", cal_triangle(base,high))
        elif menu == "4":
            done = False
            print("Exit Porgram")

            
main()
