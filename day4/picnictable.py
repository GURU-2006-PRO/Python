def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


#Removing Whitespace with strip(), rstrip(), and lstrip()
'''
Sometimes you may want to strip off whitespace characters (space, tab,
and newline) from the left side, right side, or both sides of a string. The
strip() string method will return a new string without any whitespace characters at the beginning or end. 
The lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively
'''
spam = '         Hello World         '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('pamS')) ## it remove from the starting and ending ir order does not matter 

# If we want to replace from the specific location
print(spam.replace('Spam', 'guru'))



