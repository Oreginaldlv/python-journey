expenses = [1200, 450, 800, 300]

total = 0

for expense in expenses:
    total += expense

print(f"Total Expenses: ${total}")

numbers = [10, -5, 22, -1, 0]

for num in numbers:
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")
