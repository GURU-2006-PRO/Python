## this is a guess number game
import random
secret_num=random.randint(1,20)
print('I am thinking number between 1 to 20. ')

## Guess the number 6 times 
for guesstaken in (1 , 7):
    print('Take a Guess : ')
    guess = int(input())

    if (guesstaken < secret_num):
        print('your guess number is less than original number')
    elif (guesstaken > secret_num):
        print('your guess number is less than original number')
    else:
        break

if  guess == secret_num:
    print('Good job ! You guessed number in '+str(guesstaken)+'guesses!') # i use here str() because TypeError: can only concatenate str (not "int") to str
else:
    print('Nope. The number was ' + str(secret_num))
    