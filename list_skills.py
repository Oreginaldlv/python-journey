"""Print each name in a list and its length."""

names = ["Reggie", "Ava", "Marcus", "Lina"]

for name in names:
    print(f"{name} -> {len(name)} letters")

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print(number)

for number in range (100, 0, -1):
    if number % 2 == 0:
        print(number)