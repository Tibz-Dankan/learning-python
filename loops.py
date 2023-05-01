# while loops
# use to repeat to a block of code multiple times


# # Example 1
# x=1
# while x < 10:
#     if x % 2 == 0:
#         print(str(x)+ " is an even number")
#     else:
#         print(str(x)+ " is an odd number")
# x+=1

# Example 2
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break  #used to stop the loop
print("Finished")

# Example 3
j = 0
while j < 5:
    j = j + 1
    if j == 3:
        print("Skipping")
        continue #used to stop the current iteration and moves to the next one
print(j)


# for loops
# used to iterate over a given sequence or list

# Example 1
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word)


# Example 2
str = "Testing for loops in python"
count = 0
for x in str:
    if x == "t":
        count +=1
print(count)


# range 
# used to return a sequence of numbers
# range by default starts from 0
print(list(range(10))) # prints numbers from 0 to 9, 10 is not included
print(list(range(3, 8))) # prints numbers from 3 to 7, 8 is not included
print(list(range(5, 20, 2))) # prints numbers using an interval of 2
print(list(range(20, 5, -2))) # prints numbers using an interval of 2 in decreasing order

 


