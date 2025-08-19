# # # Task 2 Commenting code and using docstring to explain
name = input("Enter your name: ")
"""Input function is to insert or collect a data"""
age = int(input("Enter your age: "))
"""Int function is to enter a whole number"""
score = int(input("Enter your test score: "))
"""Int function is to enter a whole number"""

# eligibility = (age < 18) and (score > 70)
# # """Logical operator < and  > used to combine the statements"""

# # print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# citizenship = "yes"   # """Input is used to insert a text"""
# is_a_citizen = citizenship == "yes"
# enrollment = "full time"
# is_full_time = enrollment == "full time"
# Other_schorlarships = input("not receiving any schorlarship: yes or no: ")
# currently = Other_schorlarships == "yes or no"
# academic_quali = "5 As and Bs"
# quali = academic_quali == "5 As and Bs"
# eligibility = (is_a_citizen) and (is_full_time) and (currently) and (quali)
# print(f"Application accepted:", eligibility)    # Application accepted: False

citizenship = input("Enter: ")
enrollment = input("enter: ")
other_schorlarships = input(" enter: ")
academic_quali = input("enter: ")
eligibility = (citizenship == "yes" and enrollment == "Fulltime" and other_schorlarships == "no" and academic_quali == "yes")
print(f"Application accepted", eligibility)




