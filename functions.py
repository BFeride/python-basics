def average(numbers):
    return sum(numbers) / len(numbers)

def greet(name):
    return f"Welcome, {name}!"


scores = [85, 90, 78, 92, 88]

print(greet("Farida"))
print(f"Your Score: {average(scores):.2f}")
