# Placeholder for Madlibs main.py file
print()
print("Fourth of July Parade")
print()
print("Help me finish my 4th of July parade story. I'm missing a few words:")

def madlib():
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a kitchen utensil-plural: ")
    noun2 = input("enter a noun-body part-plural: ")
    verb = input("Enter a verb-ing: ")
    noun3 = input("Enter an animal-plural: ")

    story = f"""
    Last 4th of July I went to a parade in {adj1} Amityville.
    The highlight of the parade was the “Dancing Grannies” who 
    performed to Michael Jackson’s Thriller twirling {noun1}.
    Clowns handed out candy {noun2} that made the small children scream.
    Moms were {verb} while sitting in lawn chairs.
    The blind stuntman was walking on stilts while he was juggling {noun3}. 
    I think it will be safer to stay home next year!
    """
    print(story)

while True:
    madlib()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
