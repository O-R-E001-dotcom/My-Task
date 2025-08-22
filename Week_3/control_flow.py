# Working with conditional statements
# If statement
age = 20
if age >= 18:
    print("You are eligible to vote")

# If-else Statement
wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")   # Insufficient balance
"""
This is because wallet is not greater than price
"""
if wallet <= price:
    print("Purchase completed")
else:
    print("Not successful")     # Purchase completed
"""
Wallet is lesser than price
"""
# if-elif-else
score = 30
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")    # Grade C

'''
it printed else because it is the one closer to score,
but in case the "if" is closer to the score, it will print if
'''
# Nested if
age = 19
citizen = True
if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")  # You can vote
if age <= 17:
    if not citizen:
        print("You must be a citizen to vote")
    else:
        print("You can vote")
else:
    print("Too young to vote")  # too young to vote
"""
Because he/she is less than 18
"""
if age <= 17:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")  # too young to vote

# 1 For Loop
# Iterates through each element in a LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}") # I like apple
                            # I like banana
                            # I like orange
# In a tuple
coordinates = (0.3453, -0.4333, 0.5234)
for point in coordinates:
    print(f"Point: {point}")    # Point: 0.3453
                               # Point: -0.4333
                               # Point: 0.5234
# In a dictionary
student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")    #name: Tunde
                                # age: 16
                                # grade: A
for key, value in student.items():
    print(f"{value}")  # Tunde
                        # 16
                       # A
# In a string
word = "PYTHON"
for char in word:
    print(char) #P
                # Y
                # T
                # H
                # O
                # N
# 2 While loop
# The loop started with 2. the count at the top means the number 
# it will start from, while the last count += means the number it
# will add. Always remember to end by putting the "used word" after print
count = 2
while count <= 6:
    print("Number:", count)
    count += 2          # Number: 2
                        # Number: 4
                        # Number: 6
# Incrementing with `while`
num = 1
while num <= 10:
    print(num, end=" ")         
    num +=1                 # 1 2 3 4 5 6 7 8 9 10

num = 1
while num <= 10:
    print(num, end=" ")         
    num +=2             # 1 3 5 7 9 Countdown: 10
  # Decrementing with `while`
time = 10
while time > 0:
    print("Countdown:", time)
    time -= 2           # Countdown: 8
                        # Countdown: 6
                        # Countdown: 4
                        # Countdown: 2
# While with user input
# Keep asking until the user enters a correct password.
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access Granted!")


# Keep asking the user for a name until they type "exit".
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# Break
for num in range(1, 10):
    if num == 6:
        break
    print(num)
# it stops when num equals to 6 i.e 1-5

# Continue
for num in range(1, 10):
    if num == 3:
        continue
    print(num)
# The continue means you are skipping the number "3" and continue
# till you get to 9

# Pass
for num in range(1, 6):
    if num == 3:
        pass    # it does nothing for now
    else: 
        print(num)  # 3 is skipped from the numbers

# While True
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else: 
        print("Invalid choice. Try again.")
# You can only stop running with option 3

# While True for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# Making a guess
secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Keep trying.")
# If you type the secret word which is python, it will show the
# first print, if not, it will show the second print


balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
