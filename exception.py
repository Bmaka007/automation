# def colorize(text, color):
# 	colors = ("cyan", "yellow", "blue", "green", "magenta")
# 	if type(color) is not str:
# 		raise TypeError("color must be instance of str")
# 	if type(text) is not str:
# 		raise TypeError("text must be instance of str")
# 	if color not in colors:
# 		raise ValueError("color is invalid color")
# 	print(f"Printed {text} in {color}")

# colorize("hello", "red")
# colorize(3, "red")

# #####################
# try:
# 	foobar
# except:
# 	print("PROBLEM!")
# print("after the try")

# #####################
# def get(d,key):
# 	try:
# 		return d[key]
# 	except KeyError:
# 		return None
# d = {"name": "Ricky"}
# print(get(d, "city"))

# #####################
# while True:
# 	try:
# 		num = int(input("please enter a number: "))
# 	except ValueError:
# 		print("That's not a number!")
# 	else:
# 		print("I'M IN THE ELSE!")
# 		break
# 	finally:
# 		print("RUNS NO MATTER WHAT!")
# print("Rest Of Game Logic Runs")

# #####################
# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError:
# 		print("a and b must be ints or floats")
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# print(divide(1,2))
# print(divide(1,0))
# print(divide(1,'a'))

# #####################
# def divide(a,b):
# 	try:
# 		result = a/b
# 	except (ZeroDivisionError, TypeError) as err:
# 		print("Something went wrong!")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# print(divide(1,0))
# print(divide(1,'a'))

#####################
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finish debugging)


