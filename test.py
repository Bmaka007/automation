def generate_email(username, provider="gmail"):
	email_addy = f"{username}@{provider}.com"
	return email_addy

my_email = generate_email("ipvzero")
print(my_email)