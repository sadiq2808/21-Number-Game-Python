def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose1():
    print("\n\nYOU LOSE!")
    print("Better Luck Next Time!")
    exit(0)


def check(xyz):
    i = 1

    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False

        i += 1

    return True


def start1():
    xyz = []
    last = 0

    print("\n=====SADIQ 21 NUMBER GAME =====")

    while True:
        print("\nEnter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")

        chance = input("> ")

        if chance.upper() == "F":

            while last < 20:

                print("\nYour Turn.")

                inp = int(
                    input("How many numbers do you wish to enter? (1-3)\n> ")
                )

                if not (1 <= inp <= 3):
                    print("Wrong input. You are disqualified from the game.")
                    lose1()

                print("Enter Your Numbers:")

                for _ in range(inp):
                    number = int(input("> "))

                    # Make sure numbers are consecutive
                    if last != 0 and number != last + 1:
                        print("\nYou did not enter consecutive integers.")
                        lose1()

                    xyz.append(number)
                    last = number

                    if last == 21:
                        lose1()

                print("\nYour numbers:", xyz)

                # Computer's turn
                print("\nComputer's Turn.")

                comp = 4 - inp

                for j in range(1, comp + 1):
                    xyz.append(last + j)

                last = xyz[-1]

                print("Numbers after computer's turn:", xyz)

                if last >= 20:
                    print("\nCONGRATULATIONS!!!")
                    print("YOU WON!")
                    exit(0)


        elif chance.upper() == "S":

            comp = 1
            last = 0

            while last < 20:

                print("\nComputer's Turn.")

                for j in range(1, comp + 1):
                    xyz.append(last + j)

                last = xyz[-1]

                print("Numbers after computer's turn:", xyz)

                if last == 20:
                    lose1()

                print("\nYour Turn.")

                inp = int(
                    input("How many numbers do you wish to enter? (1-3)\n> ")
                )

                if not (1 <= inp <= 3):
                    print("Wrong input. You are disqualified from the game.")
                    lose1()

                print("Enter Your Numbers:")

                for _ in range(inp):

                    number = int(input("> "))

                    if number != last + 1:
                        print("\nYou did not enter consecutive integers.")
                        lose1()

                    xyz.append(number)
                    last = number

                    if last == 21:
                        lose1()

                near = nearestMultiple(last)

                comp = near - last

                if comp == 4:
                    comp = 3

                print("\nYour numbers:", xyz)

                if last >= 20:
                    print("\nCONGRATULATIONS!!!")
                    print("YOU WON!")
                    exit(0)

        else:
            print("\nWrong choice. Please enter F or S.")




game = True

while game:

    print("\nPlayer 2 is Computer.")

    ans = input(
        "Do you want to play the 21 Number Game? (Yes / No)\n> "
    )

    if ans.lower() == "yes":
        start1()

    elif ans.lower() == "no":

        nex = input(
            "Do you want to quit the game? (Yes / No)\n> "
        )

        if nex.lower() == "yes":
            print("You are quitting the game...")
            exit(0)

        elif nex.lower() == "no":
            print("Continuing...")

        else:
            print("Wrong choice.")

    else:
        print("Wrong choice. Please enter Yes or No.")