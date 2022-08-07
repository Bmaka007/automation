def eat_junk(food):
	assert food in [
		"Rice",
		"beans",
		"potato",
		"plantain",
		"fish"
	], "food must be proper food!"
	return f"Yum I am eating {food}"

food = input("Enter A Food Please: ")
print(eat_junk(food)) 