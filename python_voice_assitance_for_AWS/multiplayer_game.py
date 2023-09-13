import random

while True:
    a = int(input("Enter a number ==> "))
    b = int(input("Enter another number ==> "))

    if a > b:
        print("Enter a number greater than the first number!")

    else:
        print("Player 1")
        chances1 = 1
        chances2 = 1
        while True:
            num1 = random.randint(a, b)
            # 1st player's turn
            while True:
                inp = int(input("Guess the number ==> "))
                if inp < num1:
                    print("Your number is smaller")
                    chances1 += 1
                    continue
                elif inp > num1:
                    print("Your number is greater")
                    chances1 += 1
                    continue
                else:
                    print("You have guessed correctly!")
                    print(f"It took you {chances1} guesses")
                    break
            num2 = random.randint(a, b)
            print("player 2")
            print(f"You have to guess your number in {chances1-1} guesses.")
            # 2nd player's turn
            while True:
                inp = int(input("Guess the number ==> "))
                if inp < num2:
                    print("Your number is smaller")
                    chances2 += 1
                    continue
                elif inp > num2:
                    print("Your number is greater")
                    chances2 += 1
                    continue
                else:
                    print("You have guessed correctly!")
                    print(f"It took you {chances2} guesses")
                    break
            break
        # results
        if chances1 > chances2:
            print("Player 2 wins the game!!")
        elif chances1 < chances2:
            print("Player 1 wins the game!!")
        else:
            print("Both players took equal number of guesses.")
    # to play again
    replay = input("press Y to play again or any key to quit ==> ")
    if replay.lower() == "y":
        continue
    else:
        print("thanks for playing.")
        break

