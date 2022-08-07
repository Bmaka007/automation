 # class User:

# 	active_users = 0

# 	def __init__(self,first,last,age):
# 		self.first = first
# 		self.last = last
# 		self.age = age
# 		User.active_users += 1

# 	def logout(self):
# 		User.active_users -= 1
# 		return f"{self.first} has logged out"

# 	def full_name(self):
# 		return f"{self.first} {self.last}"

# 	def initials(self):
# 		return f"{self.first[0]}.{self.last[0]}."

# 	def likes(self, thing):
# 		return f"{self.first} like {thing}"

# 	def is_senior(self):
# 		return self.age >=65

# 	def birthday(self):
# 		self.age += 1
# 		return f"Happy {self.age}th, {self.first}"

# print(User.active_users)
# user1 = User("Joe","Mak", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users)
# print(user2.logout())
# print(User.active_users)


# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user1.initials())
# print(user2.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()




####################

# class BankAccount:
#     def __init__(self, owner, balance = 0.0):
#         self.owner = owner
#         self.balance = balance
    
#     def getBalance(self):
#         return self.balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance


######################

# class Pet:
# 	allowed = ['cat', 'dog', 'fish', 'rat']
# 	def __init__(self, name, species):
# 		if species not in Pet.allowed:
# 			raise ValueError(f"You can't have a {species} pet!")
# 		self.name = name
# 		self.species = species

# 	def set_species(self, species):
# 		if species not in Pet.allowed:
# 			raise ValueError(f"You can't have a {species} pet!")
# 		self.species = species

# cat = Pet("Blue" "cat")
# dog = pet("Wyatt", "dog")

#########################

# class Chicken:
#     total_eggs = 0
#     def __init__(self, species, name, eggs = 0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs
    
#     def lay_egg(self):
#     	Chicken.total_eggs += 1
#     	self.eggs += 1
#     	return self.eggs

# c1 = Chicken(name="Alice", species="Partridge Silkie")
# print(Chicken.total_eggs)

#########################

# class User:
# 	active_users = 0

# 	@classmethod
# 	def display_active_users(cls):
# 		return f"There are currently {cls.active_users} active users"

# 	def __init__(self,first,last,age):
# 		self.first = first
# 		self.last = last
# 		self.age = age
# 		User.active_users += 1

# 	def logout(self):
# 		User.active_users -= 1
# 		return f"{self.first} has logged out"

# 	def full_name(self):
# 		return f"{self.first} {self.last}"

# 	def initials(self):
# 		return f"{self.first[0]}.{self.last[0]}."

# 	def likes(self, thing):
# 		return f"{self.first} like {thing}"

# 	def is_senior(self):
# 		return self.age >=65

# 	def birthday(self):
# 		self.age += 1
# 		return f"Happy {self.age}th, {self.first}"

# user1 = User("Joe","Mak", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user1 = User("Joe","Mak", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())

#########################
#Inheritance

# class Animal:
# 	cool = True

# 	def make_sound(self, sound):
# 		print(f"this animal says {sound}")

# class Cat(Animal):
# 	pass

# blue = Cat()
# blue.make_sound("MEOW")
# print(blue.cool) 

###########################

# Inheritance Example Using Super()
# class Animal:
# 	def __init__(self, name, species):
# 		self.name = name
# 		self.species = species

# 	def __repr__(self):
# 		return f"{self.name} is a {self.species}"

# 	def make_sound(self, sound):
# 		print(f"this animal says {sound}")


# class Cat(Animal):
# 	def __init__(self, name, breed, toy):
# 		super().__init__(name, species="Cat") # Call init on parent class
# 		self.breed = breed
# 		self.toy = toy

# 	def play(self):
# 		print(f"{self.name} plays with {self.toy}")



# blue = Cat("Blue","Scottish Fold", "String")
# print(blue)
# print(blue.species)
# print(blue.breed)
# blue.play()

###########################

# class User:
# 	active_users = 0

# 	@classmethod
# 	def display_active_users(cls):
# 		return f"There are currently {cls.active_users} active users"

# 	@classmethod
# 	def from_string(cls, data_str):
# 		first,last,age = data_str.split(",")
# 		return cls(first, last, int(age))

# 	def __init__(self, first, last, age):
# 		self.first = first
# 		self.last = last
# 		self.age = age
# 		User.active_users += 1

# 	def logout(self):
# 		User.active_users -= 1
# 		return f"{self.first} has logged out"

# 	def full_name(self):
# 		return f"{self.first} {self.last}"

# 	def initials(self):
# 		return f"{self.first[0]}.{self.last[0]}."

# 	def likes(self, thing):
# 		return f"{self.first} likes {thing}"

# 	def is_senior(self):
# 		return self.age >= 65

# 	def birthday(self):
# 		self.age += 1
# 		return f"Happy {self.age}th, {self.first}"

# class Moderator(User):
# 	total_mods = 0
# 	def __init__(self, first, last, age, community):
# 		super().__init__(first, last, age)
# 		self.community = community
# 		Moderator.total_mods += 1

# 	@classmethod
# 	def display_active_mods(cls):
# 		return f"There are currently {cls.total_mods} active mods"

# 	def remove_post(self):
# 		return f"{self.fullname()} removed a post from the {self.community} community"

# u1 = User("Tom", "Garcia", 35)
# u2 = User("Tom", "Garcia", 35)
# u3 = User("Tom", "Garcia", 35)
# jasmine = Moderator("Jasmine", "O'conner", 61, 'Piano')
# jasmine2 = Moderator("Jasmine", "O'conner", 61, 'Piano')
# print(User.display_active_users())
# print(Moderator.display_active_mods())

# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue","Scottish Fold", "String")
blue.play()













