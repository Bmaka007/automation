# import random
# print(random.choice(["apple", "banana", "cherry", "durian"]))

# from random import choice, randint
# print(choice(["apple", "banana", "cherry", "durian"]))

# from random import choice as pick, randint
# print(pick(["apple", "banana", "cherry", "durian"]))


# import keyword
# def contains_keyword(*args):
#     for string in args:
#         if keyword.iskeyword(string):
#             return True
#     return False

# print(contains_keyword("hello", "goodbye"))
# print(contains_keyword("hello", "goodbye", "def"))

# from termcolor import colored
# text = colored("HI THERE!", 'cyan', 'on_magenta')
# print(text)

# import termcolor
# help(termcolor) #displays info about module


# from pyfiglet import figlet_format
# from termcolor import colored


# def print_art(entry, col):
#     valid_color = ("red", "green", "yellow", "blue",
#                    "magenta", "cyan", "white")

#     if col not in valid_color:
#         col = "magenta"
#     header = figlet_format(entry)
#     header = colored(header, color=col)
#     print(header)

# entry = input("What message do you want to print:  ")
# col = input("What color?: ")
# print_art(entry, col)


# autopep8 --in-place modules.py (to be ran in cli to arrange code)
