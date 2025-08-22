
minimum_age = 16
UTME_Score = 200
candidate = '5 credits'
# Inserting details
age = int(input("enter your age: "))
score = int(input("enter your score: "))
subjects = input("do you have 5 credits? Yes or no: ").title()
required_age = (age >= 16)
post_utme = (UTME_Score > 200)
overall_performance = UTME_Score in range (200 - 320)
departmental = overall_performance
final_admission = departmental
# Checking eligibility of the candidate
eligibility = (required_age and subjects == "Yes" and post_utme and overall_performance and departmental and final_admission)
print(f"Your application: {eligibility}")