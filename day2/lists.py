# # LISTS in python
# spam = ['cat','dog','mouse','rat']
# print(spam)
# print(spam[0:4])
# print(spam[0:-1])
# print(spam[-3])
# print(spam[0:-1])
# print(spam[1:])
# print(spam[:])
# print(len(spam))

# # changing word in spam
# spam[1]='guru'
# print(spam)
# spam[-1]='sadu'
# print(spam)

# # List concatenation and Replication
# spam = [1,2,3] + ['A','B','C']
# print(spam)
# spam = ['x','y','z']*3
# print(spam)

# # deletiom from the list
# spam = ['cat','dog','mouse','rat']
# del spam[2]
# print(spam)

# # Working with list
# catName1 = 'Zophie'
# catName2 = 'Pooka'
# catName3 = 'Simon'
# catName4 = 'Lady Macbeth'
# catName5 = 'Fat-tail'
# catName6 = 'Miss Cleo'

# print('Enter the name of cat 1:')
# catName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# print('Enter the name of cat 3:')
# catName3 = input()
# print('Enter the name of cat 4:')
# catName4 = input()
# print('Enter the name of cat 5:')
# catName5 = input()
# print('Enter the name of cat 6:')
# catName6 = input()
# print('The cat names are:')
# print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
# catName5 + ' ' + catName6)

# # instead of these large code we can make it short 
# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation

# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)


# # Using for loops with list
# supplies = ['pens','staples','binders','erasers']
# for i in range(len(supplies)):
#     print('Index '+ str(i)+ ' in supplies is: ' + supplies[i])


# # the in and in not operators - we can check a particular item exist in a list or not
# spam = ['hello','hi','guru','heyas']
# print('cat' in spam)
# print('guru' in spam)
# print('guru' not in spam)

# ## the Multiple assisgnment trick
# cat = ['fat','black','loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# print(cat)

# ## Augmented Assignement Operator(+= , -= , *= etc..)
# spam = 42
# spam += 1
# print(spam)
# spam -= 1
# print(spam)
# spam *= 1
# print(spam)
# spam /= 1
# print(spam)
# spam %= 1
# print(spam)


# ## Finding value in a list with a index() Method
# spam = ['hello','hi','howdy','heyas','hi']
# print(spam.index('hello'))
# print(spam.index('hi')) ## if items are repeting then it considered the first appearing item


# ## Adding values to list with append() and insert() - can be called only list values , not on other values such as string or integers
# spam = [ 'cat','dog','bat']
# print(spam)
# spam.append('moose') #It add the item at last
# print(spam)
# spam.insert(1,'guru') # we can add item at any index through insert
# print(spam)

# ## Removing values from the list - There are 3 ways

# # 1 . del() - delete by index
# numbers = [10, 20, 30, 40]
# del numbers[1]
# print(numbers)

# # 2 . remove() - delete by value
# animals = ['cat', 'dog', 'cow']
# animals.remove('dog')
# print(animals)

# # 3 . pop() → delete AND return the item
# items = ['pen', 'pencil', 'eraser']
# x = items.pop(1)
# print(x)
# print(items)


# ## SORTING the values in a list with sort() Method :
# spam = [2 , 5 , 3.14 , 1 , -7]
# spam.sort()
# print(spam)

# spam = ['dog','elephant','monkey','apple','cat','boy']
# spam.sort()
# print(spam)

# spam.sort(reverse=True) #It helps to reverse the value but according to the alphabet not only reverse it arranges also
# print(spam)

# spam = ['Alice','ants','Bob','badgers','Carol','cats']
# spam.sort() # it sort the values according the ASCII code Values - Uppercase come before the Lowercase
# print(spam)

# ## if we want in regular alphabetical order we use sort(key=str.lower)

# ## one thing i observed that in python indentation is matters but inside list it's not matters

# # Strings are immutable and it can not be changed


'''one special thing and i knew that between the normal variable and list - list works differently
    Normal variables store values
    Lists store references (addresses)'''
## Normal Variable

spam = 42
cheese = spam
spam = 100
print(spam)  # get 100
print(cheese) # get 42

## in Lists
spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] ='hello'
print(spam)
print(cheese)
# both get the same values 


## the copy modulo's cpoy() and deepcopy() functions - if we dont want to change in original list 
import copy 
spam = ['A','B','C','D']
cheese=copy.copy(spam)
cheese[1]=42
print(spam)
print(cheese)

# Now they are the separate list and memory

