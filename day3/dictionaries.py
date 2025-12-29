# ''' a dictionary is a collection of many values. But unlike indexes for
# lists, indexes for dictionaries can use many different data types, not just
# integers. Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair'''

# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat['size'])
# print('My cat has ' + myCat['color'] + ' fur.')

# ## Dictionaries VS Lists
# '''in lists order is matter we declare variables spam and bacon and then i compared both but both are not
# same because in list order is matter'''

# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# x = (spam == bacon)
# print(x)

# '''in dictionary order is not matter we declare variables spam and bacon and then i compared both are
# same because in dictionary order is not matters at all '''
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# x = (eggs == ham)
# print(x)

# ## Now i write a code with my friend name and their birthday if someone is not in their then accordingly i update the dictionary
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name(blank to quit) :')
#     name = input()

#     if name in birthdays: ## here i check the item present in the present dictionary
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else: 
#         print("i don't have a information for ",name)

#         print('If you want to add in the existing database then tell me the birth date ')
#         bday = input()

#         birthdays[name] = bday
#         print('Birthday database updated.')
#         print(birthdays)
#     break ## i introduce to there because below program not execute and it is run in infinite loop
    
# ## The keys(),Values(), and Items() Methods
# '''There are three dictionary methods that will return list-like values of the
# dictionary’s keys, values, or both keys and values: keys(), values(), and items().
# The values returned by these methods are not true lists: They cannot be
# modified and do not have an append() method. But these data types (dict_keys,
# dict_values, and dict_items, respectively) can be used in for loops.'''

# spam = {'color':'red' , 'age':42}
# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)

# ## we pass dict_key through list()
# spam = {'color': 'red', 'age': 42}
# spam.keys()
# x = list(spam.keys())
# print(x)

# ## print the values and keys in dictionary
# spam = {'color' : 'red' , 'age' : 42}
# for v , k in spam.items():
#     print('key: '+ str(k) +' || value: ',str(v))

# ## Checking whether a key or value exists in dictionary
# spam = {'name': 'Zophie' , 'age' : 7}
# x = 'name' in spam.keys()
# print(x)
# x = 'Zophie' in spam.values()
# print(x)

# ## The get() Method 
# '''It’s tedious to check whether a key exists in a dictionary before accessing
# that key’s value. Fortunately, dictionaries have a get() method that takes two
# arguments: the key of the value to retrieve and a fallback value to return if
# that key does not exist.'''

# picnicItems = {'apples': 5, 'cups': 2}
# x = 'I am bringing '+ str(picnicItems.get('cups',0)) + ' cups'
# print(x)
# x = 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# print(x)
# # Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.

# ## The setdefault() Method
# spam = {'name':'Pooka' , 'age':5}
# if 'color' not in spam:
#     spam['color']='black'
# # these takes 3 lines but setdefault() did in one line

# spam = {'name': 'Pooka', 'age': 5}
# print('Enter the key : ')
# key = input()
# print('Enter the Value : ')
# value = input()
# print(spam.setdefault(key,value))
# print(spam)


##The number of letter in a string
message = 'The Importance of Education in Shaping Our Future Respected teachers, honorable guests, and my dear friends, Good morning to everyone present here today. Today, I stand before you to speak on a topic that touches every life, shapes every dream, and builds the foundation of every successful society — the importance of education in shaping our future Education is not just about reading books, passing exams, or getting a degree. It is about developing the ability to think, to question, to understand, and to make wise decisions. Education is the light that removes ignorance and gives direction to human life. Without education, progress becomes slow, society becomes divided, and opportunities become limited.From the moment we are born, learning becomes a part of our life. A child learns by observing, listening, and asking questions. Formal education refines this natural curiosity and converts it into knowledge, skills, and values. Schools, colleges, and universities are not just buildings — they are places where minds are trained, characters are formed, and futures are prepared.'

count = {}

for character in message :
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)
print()

## Pretty Printing
'''If you import the pprint module into your programs, you’ll have access to
the pprint()-pretty print and pformat()-pretty format functions that will “pretty print” a dictionary’s
values. This is helpful when you want a cleaner display of the items in a
dictionary than what print() provides'''
import pprint
message = 'The Importance of Education in Shaping Our Future Respected teachers, honorable guests, and my dear friends, Good morning to everyone present here today. Today, I stand before you to speak on a topic that touches every life, shapes every dream, and builds the foundation of every successful society — the importance of education in shaping our future Education is not just about reading books, passing exams, or getting a degree. It is about developing the ability to think, to question, to understand, and to make wise decisions. Education is the light that removes ignorance and gives direction to human life. Without education, progress becomes slow, society becomes divided, and opportunities become limited.From the moment we are born, learning becomes a part of our life. A child learns by observing, listening, and asking questions. Formal education refines this natural curiosity and converts it into knowledge, skills, and values. Schools, colleges, and universities are not just buildings — they are places where minds are trained, characters are formed, and futures are prepared.'

count = {}

for character in message :
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)
print(pprint.pformat(count))
