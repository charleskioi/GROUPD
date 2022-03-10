
import random
print('Welcome to the number guessing game')
number_to_guess=random.randint(1,10)
num_of_tries=3
guess=int(input('Please guess the number'))
while number_to_guess !=guess:
    print('Sorry! wrong number')
    if num_of_tries == 2:
        break
    elif guess<number_to_guess:
        print('Your guess is lower than the number')
    else:
        print('Your guess was higher than the number')
    guess=int(input('please guess again'))
    num_of_tries +=1
    if number_to_guess == guess:
        print('You win')
        print('you took',number_to_guess,'Goes to complete the game')
    else:
        print('you loose')
        print('the number you need to guess was',number_to_guess)
        print('game over')
        print('number_of_tries')

