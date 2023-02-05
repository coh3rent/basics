import random

check = True
times = 0
num = random.randint(1, 10)
while check == True:
    if times == 0:
        print("Guess a number from 1 to 10, You can only try 6 times")
        input_num = int(input("your first guess "))
        times += 1
        if  input_num == num:
            print("You guessed right! The number was " + str(num))
            print("guesses: " + str(times) )
            check = False
        elif input_num < num:
            print("More!")
        elif input_num > num:
            print("Less!")
    elif times < 6:
        input_num = int(input())
        times += 1
        if  input_num == num:
            print("You guessed right! The number was " + str(num))
            print("guesses: " + str(times) )
            check = False
        elif input_num < num:
            print("More!")
        elif input_num > num:
            print("Less!")
    else:
        print("Game over")
        check = False




