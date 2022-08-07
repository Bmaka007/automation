import pyfiglet
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

message = input("what message do you want to print ?: ")
color_sel = input("what color? ")

if color_sel == valid_colors:
	color_sel = color_sel
else:
	print("incorrect color")
	break

result = pyfiglet.figlet_format(message)
color = colored(result, clo)
print(color)



