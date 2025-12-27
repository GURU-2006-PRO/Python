for i in range(5):
    print("guru "+str(i+1))

#sum of number 
print("enter the number")
value=int(input())
total = 0
for num in range (value + 1):
    total = total + num
    
print(total)



# print random number 
import random
print("Enter a number :")
value = int(input())
for i in range(value):
    print(random.randint(1,value))

# use of sys.exit
import sys
while True:
 print('Type exit to exit.')
 response = input()
 if response == 'exit':
    sys.exit()
 print('You typed ' + response + '.')


# End keyword
print('hello',end=" ")
print('world')

# Sep keyword
print('cat','dog','mice',sep='---')

#guess number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guesstaken in range(1,7):
    guess = int(input("Enter a number : "))

    if guess < secretNumber:
        print("Your guess is low.")
    elif guess > secretNumber:
        print("Your guess is high.")
    else : 
        break

if guess == secretNumber:
    print("great you guess the number in " +str(guesstaken)+ " guesses!" )
else:
    print("Nope , the number i was thinking was "+str(secretNumber))


# the collatz sequence
def collatz(num):
    if num % 2 == 0:
        result = num // 2
        print(result)
        return result
    else:
        result = 3 * num + 1
        print(result)
        return result

num = int(input("Enter a number: "))

while num != 1:
    num = collatz(num)

