product = {
    "name": "Consulting Service",
    "price": 1500,
    "active": True
}

print(f"Product: {product['name']}")
print(f"Price: ${product['price']}")
user = {
    "name": "Reggie",
    "age": 54,
    "career": "Python Developer"
}
user = {
    "name": "Reggie",
    "age": 54,
    "career": "Python Developer"
}
user["income_goal"] = 70000
print(user)

user["age"] = 55
print(user)
for key, value in user.items():
    print(key, value)
if user["income_goal"] >= 70000:
    print("Income target defined.")
    
