instructor = {
	"name": "Colt",
	"owns_dog": "True",
	"num_courses": 4,
	"favorite_language": "Python",
	"is_hilarious": False,
	44: "my favorite number!"
}

# # for key in instructor.keys():
# # 	print(key)

# # for value in instructor.values():
# # 	print(value)

# # for item in instructor.items():
# # 	print(item)

# # for key,value in instructor.items():
# # 	print(f"key is {key} and value is {value}")


# # if "name" in instructor:
# # 	print("YES")

# # if False in instructor.values():
# # 	print("I am here")

# # clone = instructor.copy()
# # print (clone)

# # print({}.fromkeys(["email","ring"], 'unknown'))
# # print({}.fromkeys("ring", 'unknown'))

# print(instructor.get('name'))
# print(instructor.get('Colt'))  #NONE


# instructor.pop("name")
# print(instructor)

# instructor["name"] = "Colt"

##########################################################

# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# if food in bakery_stock:
#     # print(f"{bakery_stock.values()} left")
#     print("{} left".format(bakery_stock[food]))
# else:
#     print("We don't make that")

# print(bakery_stock[food])


##########################################################

# numbers = dict(first=1, second=2, third=3)
# squared_numbers = {key: value ** 2 for key,value in numbers.item()}
# print(squared_numbers)


# print({num: num**2 for num in [1,2,3,4,5]})


# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]: str2[i] for i in range(0,len(str1))}
# print(combo)

######

# instructor2 = {
# 	"name": "Colt",
# 	"owns_dog": "True",
# 	"num_courses": "four",
# 	"favorite_language": "Python",
# 	"is_hilarious": "False",
# 	"color": "my favorite number!"
# }

# yelling_instructor = {key.upper(): value.upper() for key,value in instructor.items()}
# print(yelling_instructor)

# num_list = [1,2,3,4]
# print({ num:("even" if num % 2 == 0 else "odd") for num in num_list })

# 
# value = 0
# answer = {key:value for key in 'aeiou'}
# print(answer)


# answer = {count: chr(count) for count in range(65,91)} 

