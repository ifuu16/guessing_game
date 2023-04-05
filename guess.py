import random


def guess_number():

    secret_number = random.randint(1,9)
    counter = 0

    while counter < 5:
        guess = int(input("guess a number from 1 to 9: \n"))
        if guess == secret_number:
            print(f'CORRECT!!!The secret number is {secret_number}')
            break
        elif guess < secret_number:
            print('sorry,try again the guess is too low')
        elif guess > secret_number:
            print('sorry,try again the guess is too high')
        else:
            counter += 1
            if counter == 1:
                print(f'you have tried {counter} time')
            else:
                print(f'you have tried {counter} times')
        if counter == 5:
            print(f'sorry your lifeline is up, you tried {counter} times the secret number is {secret_number}')


guess_number()


