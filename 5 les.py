
users = {
    "Andriy": "teenager",
    "Marko": "adult",
    "Oleg": "child",
    "Anna": "adult"
}

name = input("Enter name: ")

try:
    print(f"Age category: {users[name]}")
except KeyError:
    print("The person was not found")