# Comparison operators
a = 10
b = 20
print(a == b)   # False    
print(a != b)   # True 
print(a > b)    # False
print(a < b)    # True
print(a >= 10)  # True
print(a <= 10)  # True
print(b <= 20)  # True
print(b >= 20)  # True

# Use case 
score = 75
print(score >= 75)  # True
print(score < 50)   # False
print(score == 100) # False

# Assignment Operators
x = 10
print("Initial value:", x)  # Initial value: 10
x +=5
print("After x += 5:", x)   # After x += 5: 15
x -= 2
print("After x -= 2:", x)    # After x -= 2: 13
x *= 3
print("After x *= 3:", x )   # After x *= 3: 39
x /= 4
print("After x /= 4:", x)   # After x /= 4: 9.75
x %= 3
# print("After x %= 3:", x)   # After x %= 3: 0.75 
# If you divide 9.75/3 it will give 3.25, so you will
# multiply the first answer from the division (3.25) which is 
# 3 by the first number you divided with (3 * 3) = 9, minus
# the actuual answer (9.75) and the answer i 0.75
# Example
x %= 6
print("After x %= 6:", x)   # After x %= 6: 3.75

x = 4
x **= 2
print("After x **= 2:", x)     # After x **= 2: 16
x //= 3
print("After x //= 3:", x)      # After x //= 3: 5

# Use case
# Define Variables
balance = 1000
deposit = 200
withdraw = 150

deposit += withdraw
print(deposit)          # 350 i.e 200 + 150

balance -= withdraw
print(balance)          # 850 i.e 1000 + 150 
 # If u print 4rm the bck, it gives the listed amount of wat u want 2
# to print

# Logical Operators
x = 10
y = 20
print(x > 5 and y > 15) # True
print(x < 5 or y > 15)  # True
# not operator
print(not(x == 10))     # False

# Use case example
# Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Schorlarship Eligible:", eligible)   # Schorlarship Eligible: True

# Use case example 2
age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age < 25)
print("Access Granted:", can_enter) # Access Granted: True