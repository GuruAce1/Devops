def greet_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Hello, {name}! You are {age} years old.")

    if int(age) < 18:
        print("You're still young! Enjoy your time.")
    else:
        print("You're an adult now! Make the most of it.")

# Call the function
greet_user()
