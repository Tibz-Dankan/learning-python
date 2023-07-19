# Tuples
# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.

words = ("spam", "eggs", "sausages",)  # Declaring a tuple

print(words[0])   #Accessing elements in the tuple

words[1] = "cheese" #Trying to reassign a value in a tuple causes a TypeError.


# Tuples can be created without the parentheses, by just separating the values with commas.

my_tuple = "one", "two", "three"
print(my_tuple[0])

# Empty tuple
tpl = ()

