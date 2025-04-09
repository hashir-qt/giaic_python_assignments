import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print("Round ", i + 1)
        computer_num = random.randint(1, 100)
        user_num = random.randint(1, 100)
        print("Your Number is: ", user_num)
        choice = input("Do you think your Number is higher or lower? ")

        while choice != "higher" and choice != "lower":
          choice = input("Please either choose 'higher' or 'lower' ")

        higher_and_correct = choice == "higher" and user_num > computer_num
        lower_and_correct = choice == "lower" and user_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right the computer's number was ", computer_num)
            your_score = your_score + 1
        
        else:
            print("Sorry! Incorrect the computer's number was ", computer_num)
        
        print("Score: ", your_score)
        print("----------------------------")

    print("--GAME OVER--")
    if your_score == NUM_ROUNDS:
        print("Woohoo! A perfect SCORE, your Final Score: ", your_score)
    elif your_score > 2:
        print("You played really Well!, you Final Score: ", your_score)
    else:
        print("Better luck Next time, your Final Score: ", your_score)


     # TODO: Write your code here!!! :)
if __name__ == "__main__":
    main()