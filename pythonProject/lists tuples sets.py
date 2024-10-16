# Lists = [] ordered and changeable .Duplicates OK
# Set = {} unordered and immutable, but add?remove ok. NO Duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER than all.

# Lists
# fruits = ["apple","orange","banana","coconut"]
# print(fruits[0:3])
# print(dir(fruits)) these are functions are used to play with collections
# print(help(fruits))
# .append() is a method
# fruits.append("pineapple")
# print(fruits)
# fruits.insert(0,"pineapple")
# print(fruits)
# fruits.sort()---alphabetical order
# fruits.pop()-- removes the first element

# Set
# fruits = {"apple","orange","banana","coconut"}
# indexing doesn't work because we don't know where they are only add and remove the element works.

# Tuples
fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits.index("coconut"))
for fruit in fruits:
    print(fruit)
# iv ivh
