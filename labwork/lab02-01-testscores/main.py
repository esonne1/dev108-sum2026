# Instructions for Exercise 2.2

# Modify the Test Scores program so that it saves the three scores input into variables named score1, score2, and score 3. Then, add these scores to the total_score variable, instead of adding the entries to the total_score variable without ever saving them.

# Starting Code for Exercise 2.2

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score 1: "))
score1 += total_score
score2 = int(input("Enter test score 2: "))
score2 += total_score
score3 = int(input("Enter test score 3: "))
score3 += total_score

# calculate average score
total_score = (score1+score2+score3)             
average_score = round(total_score / 3)           
# format and display the result
print("======================")
print(f"Total Score:  ",total_score,{score1},{score2},{score3})
print("Average Score:", average_score)
print()
print("Bye")
