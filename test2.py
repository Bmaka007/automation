def add_mul_div(num1, num2):
	mul = num1 * num2
	add = num1 + num2
#	div = num1 / num2

	return add, mul

x, y = add_mul_div(10,15)

print(f"This added result of the function is {x}")
print(f"...and the multiplied result of the function is {y}")
