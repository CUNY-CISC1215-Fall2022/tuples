# A tuple is like a list, but it cannot be changed later:
my_tuple = (1, 2)
print("my_tuple:", my_tuple)
print("my_tuple[0]:", my_tuple[0])
print("my_tuple[1]:", my_tuple[1])

# These operations will fail:
# my_tuple[0] = 12
# my_tuple.append(1)

print()
# Tuples are created with the zip function, which is used to combine
# lists:
a = [3, 8, 2, 0]
b = [9, 1, 10, 8]

for left, right in zip(a, b):
    print("Zip iteration:", left, right)


print()
# Tuples are used in scattering and gathering with function arguments.
# Scattering:
def max(a, b):
    if a > b:
        return a
    return b

my_numbers = (100, 1)
# Scatter the tuple values (100, 1) into the arguments a and b for max()
result = max(*my_numbers)
print("max(100, 1):", result)

print()
#Gathering:
# The function print_all requires one parameter, a.
# After a, it can accept any number of arguments, which it
# will save in a tuple.
def print_all(a, *args):
    print(a, args)

print("print_all() with gathering:")
print_all(10)
print_all(10, 100)
print_all(10, 100, 2)


print()
# Tuples can be elements of other data structures.
# For example, we can iterate over a list of tuples:

my_tuples = [("Matt", 36), ("Alice", 25), ("Bob", 41)]

for name, age in my_tuples:
    print("Name: " + name, "Age: " + str(age))


print()
# We can return tuples from functions:
def integer_division(numerator, denominator):
    result = numerator // denominator
    remainder = numerator % denominator
    return (result, remainder)

result, remainder = integer_division(9,2)
print("9/2 result", result, "remainder")


print()
# The dictionary method items() returns a list of
# tuples containing all its key/value pairs:
my_dict = {'Matt': 36, 'Alice': 25, 'Bob': 41}
print("my_dict key/value pairs:")
for name, age in my_dict.items():
    print(name + " is " + str(age))


# We can also use a list of 2-element tuples to build a dictionary:
pairs = [('Matt', 36), ('Alice', 25), ('Bob', 41)]
print()
print("Dictionary made from tuples:", dict(pairs))