# def sum(n, func):
# 	total = 0
# 	for num in range(n):
# 		total += func(num)
# 	return total

# def square(x):
# 	return x*x

# def cube(x):
# 	return x*x*x	

# print(sum(10,square))
# print(sum(10,cube))

###################################

# from random import choice
# def make_laugh_func(person):
# 	def get_laugh():
# 		laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
# 		return f"{laugh} {person}"

# 	return get_laugh

# laugh = make_laugh_func("Linda")

# print(laugh())

##################################
#Deco_before#
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# def greet():
#     print("My name is Colt.")

# def rage():
# 	print("I HATE YOU!")

# # we are decorating our function 
# # with politeness!
# greet = be_polite(greet)

# polite_rage = be_polite(rage)
# polite_rage()


#Deco_after#
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# @be_polite
# def greet():
#     print("My name is Colt.")

# @be_polite
# def rage():
# 	print("I HATE YOU!")

# greet()
# rage()

##################################

# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return wrapper

# @shout
# def greet(name):
#     return f"Hi, I'm {name}."

# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."

# @shout
# def lol():
# 	return "lol"

# print(greet("todd"))
# print(order(side="burger", main="fries"))
# print(lol()) 

###############################



