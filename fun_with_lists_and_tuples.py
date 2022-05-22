#Fun with Lists and Tuples
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

lst1 = []
list_size = int(input('Please provide the detail of how many sets of tuple data will be provided as input:'))
for i in range(list_size):
    a = tuple(input('Please provide the first value of each set of tuple:'))
    b = tuple(input('Please provide the second value of each set of tuple:'))
    c = a + b
    lst1.append(c)
print("Your provided data:",lst1)

for i in range(len(lst1)): #0
    for j in range(0,len(lst1)-i-1): #1

        if (lst1[j][-1] > lst1[j+1][-1]):

            temp = lst1[j] 

            lst1[j] = lst1[j+1] 

            lst1[j+1] = temp 

print("Your sorted output data : ",lst1)