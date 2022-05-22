# Make Your Own mini-Dictionary
# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dictionary = {} 
keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values=[]

for i in range(97,97+len(keys)):
    val = i
    values.append(val)

dictionary = dict(zip(keys,values))
print("Dictionay with Alphabetical keys and corresponding ASCII values :",dictionary)

