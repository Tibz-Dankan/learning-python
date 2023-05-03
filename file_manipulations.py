# Opening files
open("filename.txt")

# open file in the write mode
open("filename.txt", "w")

# open file in the read mode
open("filename.txt", "r")
open("filename.txt")

# open file in the binary write mode
open("filename.txt", "wb")

# closing  files
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()   # closing the file


# Note: modes r and w are used for reading from and writing to only text(.txt) files
# Note:  modes wr and wb  are used for reading from and writing to binary files such image and sound


# Reading files
file = open("filename.txt", "r")
file.read()   # reading a file
print("Re-reading")
print(file.read())
print("Finished")
file.close()

# output for the above code
# >>>
# Re-reading

# Finished
# >>>


# Reading file by line
file = open("filename.txt", "r")
print(file.readlines())
file.close()

# output for the above code
# >>>
# ['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
# >>>
