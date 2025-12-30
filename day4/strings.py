# spam = ' This is a Alice's cat' - this gives an error because we use apostophe s so python understand and end the statement and not run the rest of sentence
# So we use " " to solve this issue
spam = "This is a Alice's cat"
print(spam)

# Escape Character - we use this to avoid halucination like up
'''\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash'''

## Raw Strings - place r before string then the statement print as it is , no affect to add from escape characters
print(r'This is Guru \n and he is god')
  

## Multiline strings- use triple times single inverted , not one time double inverted comma and one time single inverted comma- single quote character in Eve's does not need to be escaped. Escaping single and double quotes is optional in multiline strings. The following print() call would print identical text but doesn’t use a multiline string
'''Byte Quest – AI Vibe Coding Challenge 2026 is a 24-hour online hackathon designed for university students who are passionate about coding, innovation, and real-world problem solving. This challenge gives participants the opportunity to combine their programming skills with modern AI tools and transform ideas into practical solutions within a limited time frame. Organized by the GeeksforGeeks Campus Body,RBU the event promises a fast-paced, competitive, and collaborative coding experience.'''

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

## Indexing and Slicing String
spam = 'Hello World'
print(spam[0])
print(spam[0:5])
print(spam[ 3:5])
print(spam[:-6])
print(spam[:-6])
print(spam[6:])
print(spam[:])

"""By slicing and storing the resulting substring in another variable, you can
have both the whole string and the substring handy for quick, easy access."""
fizz = spam[5:11]
print(fizz)

## The in and not in operators with string
x = 'hello' in 'hello world'
print(x)

x = 'guru' not in 'guru vinod sawarkar'
print(x)

## Useful Strings method (The upper(), lower(), isupper(), and islower() String Methods)
spam = 'Hello World'
print(spam.upper())
print(spam.lower())

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
 print('I feel great too.')
else:
 print('I hope the rest of your day is good.')

'''The isupper() and islower() methods will return a Boolean True value
if the string has at least one letter and all the letters are uppercase orlowercase repectively '''
spam = 'Hello World'
print(spam.islower())

spam = 'hello world'
print(spam.islower())

print('abc12345'.islower())

spam = 'Hello'
print(spam.upper().lower().upper().lower().lower())

## The isX String Methods
'''
•	 isalpha() returns True if the string consists only of letters and is not blank.
•	 isalnum() returns True if the string consists only of letters and numbers and is not blank.
•	 isdecimal() returns True if the string consists only of numeric characters and is not blank.
•	 isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
•	 istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
'''
spam = 'hello'
print(spam.isalpha())

spam = 'hello123'
print(spam.isalpha())

spam = 'hello123'
print(spam.isalnum())

spam = '123'
print(spam.isdecimal())

spam = 'This Is Title Case'
print(spam.istitle())

spam = 'This Is not Title Case'
print(spam.istitle())

## program of taking user , age and password with condition
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

## The startswith() and endswith() String Methods
spam = 'Hello world!'
print(spam.startswith('Hello'))

spam = 'abcdef'
print(spam.endswith('ef'))

spam = 'Hello world!'
print(spam.startswith('Hello'))

## The join() and split() String Methods
spam = ', '.join(['cats', 'rats', 'bats'])
print(spam)

spam = ' || '.join(['cats', 'rats', 'bats'])
print(spam)

spam = '_'.join(['cats', 'rats', 'bats'])
print(spam)

spam = '$$'.join(['Moti','Chain','Mota','Paisa'])
print(spam)

spam = 'My name is Simon'.split() ## By default in split there is space is given
print(spam)

spam = 'MyABCnameABCisABCSimon'.split('ABC')
print(spam)

# A common use of split() is to split a multiline string along the newline characters.
spam = '''Dear Alice, How have you been? I am fine. There is a container in the fridge
that is labeled "Milk Experiment" Please do not drink it. Sincerely, Bob'''
print(spam.split('\n'))


## Justifying Text with rjust(), ljust(), and center()
spam = 'hello Guru'
print(spam.rjust(10))
print(spam.rjust(30))
print(spam.rjust(50))
print(spam.rjust(70))
print(spam.rjust(90))
'''
'Hello'.rjust(10) says that we want to right-justify 'Hello' in a string of
total length 10. 'Hello' is five characters, so five spaces will be added to its
left, giving us a string of 10 characters with 'Hello' justified right.
'''
spam = 'Bye Guru'
print(spam.ljust(10))
print(spam.center(100))

'''An optional second argument to rjust() and ljust() will specify a fill
character other than a space character.
'''
spam = 'hello'
print(spam.rjust(50, '='))

'''
The center() string method works like ljust() and rjust() but centers
the text rather than justifying it to the left or right. 
'''
spam = ' hello '
print(spam.center(100,'|'))

#These methods are especially useful when you need to print tabular data that has the correct spacing
