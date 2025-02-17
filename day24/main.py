# file = open("my_file.txt")
#
# contents = file.read()
# print(contents)
# file.close()

# ======= OR =======

with open("my_file.txt") as file:   #open in read mode  -> mode=r
    contents = file.read()
    print(contents)


with open("my_file.txt", mode="w") as file:
    file.write("\nNew write") # inlocuieste ce e in fisier cu ce am scris

with open("my_file.txt", mode="a") as file:
    file.write("\nNew write2")  #appends at the file the new write

with open("new_file.txt", mode="w") as file:
    file.write("\nNew write") #create a new file with this line


