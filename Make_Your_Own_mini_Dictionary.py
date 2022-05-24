# Make Your Own mini-Dictionary
# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dictionary = {} 
keys = []
values=[]

for i in range(97,123):
    keys.append(chr(i))
    values.append(i)

dictionary = dict(zip(keys,values))
print("Dictionay with Alphabetical keys and corresponding ASCII values :",dictionary)

