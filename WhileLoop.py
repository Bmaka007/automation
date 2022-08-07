#i = 0
#while i <= 5:
#	i += 1
#	print(i)


#x = 0
#while x < 11:
#	x += 2
#	print(x)


#from random import randint  # use randint(a, b) to generate a random number between a and b
 
#number = 0 #store random number in here, each time through
#i = 0  # i should be incremented by one each iteration
 
#while number != 5: #keep looping while number is not 5
#    i += 1
#    number = randint(1, 10) #update number to be a new random int from 1-10

#x = 0

#for i in range(1,10,2):
#	x += i
#print(f"the addition of the odd number is: {x}")


#x = "\U0001f600"
#for i in range(1,10):
#	output = i * x
#	print(f" {output}")


#colors = ["purple", "teal", "magenta", "crimson", "emerald"]
#index = 0
#while index < len(colors):
#	print(f"{index}: {colors[index]}")
#	index += 1

# colors = ["purple", "teal", "magenta", "crimson", "emerald"]
# result = ""
# for color in colors:
# 	result = result+color
# print (result.upper())


# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # Define your code below:
# result =""
# for sound in sounds:
#     result = result + sound
# print (result.upper())

# instructors = ['ashley', 'matt', 'michael']
# for instructor in instructors:
# 	print(instructor[0].upper() + instructor[1:])

# instructors = ['ashley', 'matt', 'michael']
# for instructor in instructors:
# 	print(instructor.capitalize())


# ex = [num*10 for num in [1,2,3,4,5]]
# print(ex)

# numbers = [1, 2, 3, 4, 5, 6]
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# x = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# print(x)


# num1 = [1,2,3,4]
# num2 = [3,4,5,6]

# answer = []
# for num in [1,2,3,4]:
# 	if num in [3,4,5,6]:
# 		answer.append(num)
# print(answer)

# words = ["Elie", "Tim", "Matt"]
# answer2 = []
# for word in words:
# 	answer2.append(word.lower()[::-1])
# print (answer2)


# answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
# #the slice [::-1] is a quick way to reverse a string
# answer2 = [val.lower()[::-1] for val in ["Elie", "Tim", "Matt"]]
# print (answer2)

# answer = [num for num in range(1,100) if num % 12 ==0]
# print(answer)


# answer = [val for val in "amazing" if val not in ['a','e','i','o','u']]
# print(answer)

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
 
# # concat first and last name with a space
# full_name = artist["first"] + " " + artist["last"]


# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
 
# full_name = f"{artist['first']} {artist['last']}"

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!
# # Use a loop to add together all the donations and store the resulting number in a variable called total_donations
# total_donations = 0
# for y in donations.value():
#     total_donations = total_donations + y
# print (total_donations)


# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# if food in bakery_stock:
#     print("{} left".format(bakery_stock[food]))
# else:
#     print("We don't make that")

# #####################
# # List Comprehension
# #####################

# numbers = [1, 2, 3, 4, 5, 6]
# even = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]

# <action-num> for num in numbers

# [num*2 if num % 2 ==0 else num/2 for num in numbers]


# a = '{}'.join(["cool", "dude"]) #whatever is inbetween the '' will be used to join the words
# print(a)

# with_vowels = "This is so much fun!"
# a = ''.join(char for char in with_vowels if char not in "aeiou")
# print (a)
 
# board = [[num for num in range(1,4)] for val in range(1,4)]
# print(board)

# board2 = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
# print(board2)

# ##########################
# # Dictionary Comprehension
# ##########################

#d.clear, d.copy

# new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
# print (new_user)

# new_user2 = {}.fromkeys(['name'], 'unknown')
# print (new_user2)

# instructors = {
# 	"name": "Colt",
# 	"owns_dog": "True",
# 	"num_courses": 4,
# 	"favorite_language": "Python",
# 	"is_hilarious": False,
# 	'songs': [
# 		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
# 		{'title': 'song2', 'artist': ['em', 'dre'], 'duration': 2.5}
# 	# 44: 'my favorite number!'
# 	]
# }


# a = instructors.get('name')
# print (a)

# b = instructors.pop("name")
# print(instructors)

# c = instructors.popitem() random remove
# print(instructors)

# person = {"city": "hamilton"}
# person.update(instructors)
# print(person)
# print(instructors)

# for song in instructors['songs']:
# 	print(song['duration'])

# a = {num: num**2 for num in [1,2,3,4,5]}
# print(a)

# num_list = [1,2,3,4]
# d = { num:("even" if num % 2 == 0 else "odd") for num in num_list }
# e = { num:("even" if num % 2 == 0 else "odd") for num in range(1,100)}
# print(d)
# print(e)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# answer = {list1[i]: list2[i] for i in range(0,3)}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {thing[0]: thing[1] for thing in person}
# print(answer)

# answer = {char:0 for char in 'aeiou'}

# answer = {num: chr(num) for num in range(65,91)}
# print(answer)

###############################
#Function
###############################

# def generate_evens():
#     even = [num for num in range(1,50) if num % 2 == 0]
#     return even
# print(generate_evens())

# def yell(single):
#     return f"{single}".upper()+'!'

# print(yell("jide"))

# def speak(animal):
#     if animal == "pig":
#         return "oink"
# print(speak("pig"))


# def return_day(num):
#     days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     # Check to see if num valid
#     if num >= 0 and num <= len(days):
#         # use num - 1 because lists start at 0 
#         return days[num]
#     return None
# print(return_day(0))



# def capitalize(string):
#     return string[0].upper() + string[1:]

# print(capitalize("jide"))

# def compact(list1):
#     for i in list1:
#         if i == False:
#             list1.remove(i)
#     	return list1
# print(compact([0,1,2,"",[], False, {}, None, "All done"]))


# def contains_purple(*nums):
# 	if "purple" in nums:
# 		return True
# 	return False
# print(contains_purple(25, "purple"))


# def combine_words(word,**kwargs):
#     if "prefix" in kwargs:
#         return kwargs["prefix"] + word
#     elif "suffix" in kwargs:
#         return word + kwargs["suffix"]
#     else:
#         return word

# print (combine_words("child", prefix="man"))


# def square(num):
#     return num * num
# #or
# lambda num: num * num

# people = ["jide", "seun"]
# peeps = map(lambda name: name.upper(), people)
# list(peeps)


# decrement_list = map(lambda num: num-1, nums)
# list(decrement_list)

# a_names = filter(lambda n: n[0]=='a', people)
# list(a_namesl)


# def remove_negatives(l):
#     a_num = filter(lambda n: n >= 0, numbers)
#     list(a_num)


# raise ValueError('You Dey Crase')
  

