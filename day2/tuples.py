''' Tuples - tuples is almost identical like list data type , except in few ways 
    1 . tuples are typed with parenthesis, ( ) 
    2 . tuples - immutable(can not be changed)  '''

print(type(('hello',))) #if give , the python treats that it is tuple
print(type('hello')) #otherwise it treats normal

value = ('hello','42','0.5')
print(value[0])
print(value[1:3])
print(len(value))

## if we want to modify the tuple then we can convert into list and then do the operations


## passing refereces 
def change(x):
    x = 10

a = 5
change(a)
print(a)
# integers can not be modified and only reassigned

def add_item(lst):
    lst.append("apple")

fruits = ["banana", "mango"]
add_item(fruits)
print(fruits)


'''because of tupple immutable there is only two operations that are count and index'''
t = (1, 2, 2, 3)

print(t.count)
print(t.count(2))   # 2
print(t.index(3))   # 3

## the copy modulo's cpoy() and deepcopy() functions
