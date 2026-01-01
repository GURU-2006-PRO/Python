# print the second maximum number even if the the number of maximum is repeated

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
unique = list(set(arr))
unique.sort()

if unique[-1] > unique[-2]:
    print(unique[-2])

'''
# This is better approach i think
arr = [5, 3, 9, 9, 7, 5]

unique = list(set(arr))   # remove duplicates

if len(unique) < 2:
    print("Second maximum does not exist")
else:
    unique.sort()
    print(unique[-2])
'''