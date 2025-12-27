print("Guru Sawarkar")

print("hello, how are you?")
print("what is your name?")
name = input()
print("Nice to meet you, " + name)
print(len(name))

print() ## to leave one line break

print("what is your age ? ")
age=input()
print("your age in 2025 is " + age + " and in 2026 is " +str((int(age)) + 1))

# print('I am ' + 29 + ' years old.')
#PS D:\pyhton> python -u "d:\pyhton\day1.py"
# Traceback (most recent call last):
#   File "d:\pyhton\day1.py", line 15, in <module>
#     print('I am ' + 29 + ' years old.')
#           ~~~~~~~~^~~~
# TypeError: can only concatenate str (not "int") to str
# PS D:\pyhton> 


print('I am ' + str(29) + ' years old.') 
# this always work because we converted here int to the string

num = (4 < 5) and (5 < 6) 

print(num)

print("Enter the name : ")
name = input()
if name == 'Alice':
  print('Hi, Alice.')
else:
  print('sorry , you not guess match word')

# elif sentence 
print("Enter the age ")
age= int(input())      # always remember when takes input from user it by default take as as string but here i want to typecast into integer

if age < 12:
    print("bro you are kiddo")
elif age<18 and age>=12:
    print("bro you are in your teenage")
elif age>18 and age<60 :
    print("bro you are mature and you can vote now.")
else :
    print("ohh ! bro enter a valid age")

while True:
    print('Please type your name.')
    name = input()
    if name == 'guru':
        break
print('Thank you!')


while True:
    print('Who are you? ')
    name = input()
    if name != 'guru':
        continue
    print("hello Guru , tell me your password")
    password = input()
    if password == 'gurupro':
        break
print("thank you !!")
