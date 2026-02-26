"""Create a car dictionary and print a formatted summary."""

car = {
    "make": "Tesla",
    "model": "Model 3",
    "price": 38990,
    "electric": True,
}

print(
    f"Car: {car['make']} {car['model']} | "
    f"Price: ${car['price']:,} | "
    f"Electric: {car['electric']}"
)