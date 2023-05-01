# Lists --> used to store items.

words = ["come", "go", "journey", "?"]

# items in a list are accessed via index
print(words[1])  #prints go

# note: characters in a string can also be like in lists

name = "Dankan"
print(name[2]) #prints n

# note: a list can items of different type

# List operations

# Reassigning items at a given index
nums = [7,7,7,7,7,7,7]
nums[2] = 5
print(nums) #prints [7,7,5,7,7,7,7]

# adding multiplying lists
nums1 = [1,2,3]
print(nums1+[4,5,6])  #prints [1,2,3,4,5,6]
print(nums1*3)  #prints [1,2,3] [1,2,3] [1,2,3]

# check for item in the list

words2 = ["spam", "egg", "spam"]
print("spam" in words2)    #prints True
print("tomato" in words2)  #prints False

# check for item not in the list
nums2 = [1, 2, 3, 4]
print(not 4 in nums2)
print( 4 not in nums2)
print(not 7 in nums2)
print( 7 not in nums2)

# List functions
nums3 = [5,7,8,9, 8]

nums3.append(10) #prints [5,7,8,9,10], adds 10 to the list
print(len(nums3)) #prints the number of items in the list
index =1
words.insert(index, 6) #prints [5,6,7,8,9,10], inserts 6 to at index 1(position 2) in the list

letters = ["p","q","r","s",'t',"u"]
print(letters.index("r")) #prints index 2
print(letters.index("p")) #prints  index 1
print(letters.index("z")) # Raises a valueError

# other methods
print(max(nums3))  # returns a maximum value
print(min(nums3))  # returns a minimum value
print(nums3.count(8))  # returns number of times an item occur in the list
print(nums3.remove(7))  # remove an item(7) from the list 
print(nums3.reverse())  # reverse items in a list