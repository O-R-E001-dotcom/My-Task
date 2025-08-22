name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))
eligibility = (age < 18) and (score > 70)
while True:
    academic_quali = input("Do you have atleast 5 As and Bs? Enter yes or no: ").title()
    if academic_quali == "Yes":
        print("Noted")
# citizenship = " "
    citizenship = input("enter country: ").title()
    if citizenship == "Nigeria":
# enrollment = ""
     enrollment = input("Fulltime gard or not: ").title()
    if enrollment == "Fulltime":
# other_schor = ""
        other_schor = input("Yes or no: ").title()
    if other_schor == "No":
        print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nCountry; {citizenship}\nEnrollement: {enrollment}\nOther: {other_schor}\nAcademic Qualification: {academic_quali}\nEligible: {eligibility}")
        break
    else:
       print("Schorlarship not awarded")


# """Input function is to insert or collect a data"""

