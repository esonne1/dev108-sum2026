# starting file for lab 6
import nameformat

def main():
    print("The NameFormat module\n")

    # Ask for user input once
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")

    choice = 0

    while choice != 5:
        print("\n* * MENU * *")
        print("1 - Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - Read Documentation")
        print("5 - Exit")

        try:
            choice = int(input("What is your choice? "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            print(nameformat.sayHello(first))

        elif choice == 2:
            print(nameformat.fullName(first, last))

        elif choice == 3:
            print(nameformat.lastNameFirst(first, last))

        elif choice == 4:
            print("\nMODULE DOCUMENTATION:")
            help(nameformat)
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)

        elif choice == 5:
            print("Goodbye!")

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the program
main()

