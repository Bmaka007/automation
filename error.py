# def colorize(text,color):
# 	colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
# 	if type(color) is not str:
# 		raise TypeError("color must be instance of str")
# 	if type(text) is not str:
# 		raise TypeError("text must be instance of str")
# 	if color not in colors:
# 		raise ValueError("color is invalid color")
# 	print(f"Printed {text} in {color}")
# colorize("hello", "cyan")
# colorize(34, "red")



# try:
# 	foobar
# except:
# 	print("PROBLEM")
# print("after the try ")



# def get(d,key):
# 	try:
# 		return d[key]
# 	except KeyError:
# 		return None
# d = {"name": "Ricky"}
# print(get(d, "name"))
# print(get(d, "city"))



# while True:
# 	try:
# 		num = int(input("please enter a number: "))
# 	except ValueError:
# 		print("That's not a number!")
# 	else:
# 		print("GOOD JOB")
# 		break
# 	finally:
# 		print("RUNS NO MATTER WHAT!")



# def divide(a,b):
# 	try:
# 		return a/b
# 	except ZeroDivisionError as err:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print (err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# print(divide(1,2))
# print(divide(1,'a'))



# def divide(a,b):
# 	try:
# 		return a/b
# 	except (ZeroDivisionError, TypeError) as err:
# 		print("Something went wrong!")
# 		print (err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# print(divide(1,0))
# print(divide(1,'a'))


# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

# def add_numbers(a,b,c,d):
# 	import pdb; pdb.set_trace()
# 	return a + b + c + d
# add_number(1,2,3,4)	



# def divide(num1, num2):
#     try:
#         return num1/num2
#     except TypeError:
#         print("Please provide two integers or floats")
#     except ZeroDivisionError:
#         print("Please do not divide by zero")

# print(divide(4,"a"))

