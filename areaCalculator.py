print("==========" \
" Area Calculator " \
"===========")

Triangle = 0
Rectangle = 0
Square = 0
Circle = 0

print(" 1. Triangle \n 2. Rectangle \n 3. Square \n 4. Circle \n 5. Exit")

input_choice = int(input("Which shape's area do you want to calculate? "))

if input_choice == 1:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
elif input_choice == 2:
    base = float(input("Enter the base of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    area = base * height
    print(f"The area of the rectangle is: {area}")
elif input_choice == 3:
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
elif input_choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area}")
elif input_choice == 5:
    print("Exiting...")
else:
    print("Invalid choice. Please try again.")