
print("=== List Example ===")
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")           # Add item
fruits[1] = "blueberry"           # Modify item
print("Fruits List:", fruits)
print("Second Fruit:", fruits[1])


print("\n=== Tuple Example ===")
colors = ("red", "green", "blue")
print("Colors Tuple:", colors)
print("First Color:", colors[0])



print("\n=== Dictionary Example ===")
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}
student["age"] = 22  
student["email"] = "alice@example.com" 
print("Student Dictionary:", student)
print("Student Name:", student["name"])


print("\n=== Set Example ===")
numbers = {1, 2, 3, 2, 4}
numbers.add(5)
numbers.discard(2)  
print("Numbers Set:", numbers)
print("Is 3 in set?", 3 in numbers)
