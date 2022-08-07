# with open("note.txt", "w") as file:
# 	file.write("Writing files is great\n")
# 	file.write("Here's another line of texr\n")
# 	file.write("Closing now, goodbye!")


# # w - writes and erases existing contents
# with open("note.txt", "w") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR
# with open("note.txt", "a") as file:
# 	file.seek(0)
# 	file.write(":)\n")

# r+ read and write
# with open("note.txt", "r+") as file:
# 	file.write(":)")
# 	file.seek(10)
# 	file.write(":(")

# r+ will not create a file if it doesn't exist
# with open("hello.txt", "a") as file:
# 	file.write("HELLO!!!")


#Function to copy from one file to another
# def copy(file_name, new_file_name):
#     with open(file_name) as file:
#         text = file.read()
    
#     with open(new_file_name, "w") as new_file:
#         new_file.write(text)


def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])