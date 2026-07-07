import random

print("===========")
print(" Rock Paper Scissors ")
print("===========")

print("1. Rock")
print("2. Paper")
print("3. Scissors")

input_choice = int(input("Pick a number: "))

computer = random.randint(1, 3)

choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

if input_choice not in choices:
    print("Invalid choice.")
else:
    print("You choose :", choices[input_choice])
    print("CPU choose :", choices[computer])

    if input_choice == computer:
        print("Draw!")
    elif (
        (input_choice == 1 and computer == 3) or
        (input_choice == 2 and computer == 1) or
        (input_choice == 3 and computer == 2)
    ):
        print("You Win!")
    else:
        print("CPU Wins!")