'''How would you assign the value 'hello' as the third value in a list stored
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)'''
spam = [2,4,6,8,10]
spam.insert(3,'hello')
print(spam)

'''For the following three questions, let’s say spam contains the list ['a',
'b', 'c', 'd'].
3. What does spam[int(int('3' * 2) / 11)] evaluate to?
4. What does spam[-1] evaluate to?
5. What does spam[:2] evaluate to?'''

spam = ['a','b','c','d']
print(spam[int(int('3' * 2) / 11)]) 
print(spam)

print(spam[-1]) ## last value
print(spam[:2]) # starting from last and then print accordingly

'''For the following three questions, let’s say bacon contains the list
[3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
7. What does bacon.append(99) make the list value in bacon look like?
8. What does bacon.remove('cat') make the list value in bacon look like?'''
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')
print(bacon)
bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)

'''grid = [['.', '.', '.', '.', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['.', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.']]
        write the code of it '''

# Define the grid (list of lists)
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

# Print the picture by rotating the grid
for column in range(len(grid[0])):     # number of columns
    for row in range(len(grid)):       # number of rows
        print(grid[row][column], end='')
    print()  # move to next line

