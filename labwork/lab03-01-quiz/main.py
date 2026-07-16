# Create a simple 5 question math or multiple choice quiz following th
print("Math Quiz")
print()
# ask if they want to play
ans = input("Would you like to take a math quiz?y/n ")
if ans.lower() == "y":
    print("Okay, let's play!")
elif ans.lower() == "n":
    print("Sorry. Maybe later.")
else:
    print("Invalid entry. Please restart")
# Math Questions
# initialize a counter
counter = 0
print()
q1 = int(input("Math Question 1: What is 5 X 5? "))
if q1 == 25:
    print("Good job! You are right")
    counter += 1
else:
    print("Sorry, that is wrong. The answer was 25.")
q2 = int(input("Math Question 2: What is 150/3? "))
if q2 == 50:
    print("Good job! You are right")
    counter += 1
else:
    print("Sorry, that is wrong. The answer was 50.")
q3 = int(input("Math Question 3: What is 33 X 10? "))
if q3 == 330:
    print("Good job! You are right")
    counter += 1
else:
    print("Sorry, that is wrong. The answer was 330.")
q4 = int(input("Math Question 4: What is 21/3? "))
if q4 == 7:
    print("Good job! You are right")
    counter += 1
else:
    print("Sorry, that is wrong. The answer was 7.")
q5 = int(input("Math Question 5: What is 40+50+60? "))
if q5 == 150:
    print("Good job! You are right")
    counter += 1
else:
    print("Sorry, that is wrong. The answer was 150.")
print("Your score is: ",counter)
print("Thanks for playing")
if counter == 5:
    print("You are a rock start!")
elif counter == 4:
    print("Great job!")
elif counter == 3:
    print("Almost there!")
elif counter == 2:
    print("Keep studying")
elif counter == 1:
    print("Don't give up!")













