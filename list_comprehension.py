#[_ for _ in _]

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)


# friends = ['ashley', 'matt', 'michael']
# print([friend[0].upper() + friend[1:] for friend in friends])


# numbers = [1, 2, 3, 4, 5, 6]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# print(evens)
# print(odds)

# print([num*2 if num % 2 == 0 else num/2 for num in numbers])


# with_vowels = "This is so much fun!"
# num_left = ''.join(char for char in with_vowels if char not in "aeiou")
# print(num_left)


# answer = [letter[0] for letter in ["Elie", "Tim", "Matt"]]


# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
# print(answer)

# words = ["Elie", "Tim", "Matt"]
# answer2 = [word[::-1].lower() for word in words]
# print(answer2)


# print([num for num in range(1,101) if num % 12 == 0])


# print([char for char in "amazing" if char not in "aeiou"])


# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[print(val) for val in l] for l in nested_list]


print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
print([["*" for x in [1,2,3]] for i in range(5,8)])