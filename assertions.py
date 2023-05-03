# An assertion is the sanity check you can turn or off when have finished testing a program

# An assertion raises an exception when the results comes false

# Example 1
print(1)
assert 2+2 == 4
print(2)
assert 1+1 == 3
print(3)


# Example 2
temp = -10
assert (temp >= 0), "Colder than absolute zero!"
