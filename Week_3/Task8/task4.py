# Task 4
student = {}
# Collecting details
name = input("your name: ")     # Ada
age = int(input("enter your age: "))    # 23
scores = [70, 80, 90]
student = {
    "name" : name,
    "age": age,
    "scores": scores
    
    }

# has_passed = (scores >= 50)
average_score = 50
passed = (average_score >= 50)
teenager = (age > 13) and (age < 20)
print(f"Name: {name}\nAge: {age}\nScores: {scores}\nPassed: {passed}\nTeenager: {teenager}")