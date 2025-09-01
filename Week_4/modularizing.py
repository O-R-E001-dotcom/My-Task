# # # # range()
# # # for t in range(5):
# # #     print(t)            # 0
# # #                         # 1
# # #                         # 2
# # #                         # 3
# # #                         # 4
# # # # zip()
# # # names = ["Esther", "Presh", "Ken"]
# # # scores = [34, 56, 46]
# # # for n, s in zip(names, scores):
# # #     print(n, "scored", s)   # Esther scored 34
# # #                              # Presh scored 56
# # #                             # Ken scored 46
# # # state = ["Ogun", "Oyo", "Ondo"]
# # # vote = [12, 14, 15]
# # # for s, v in zip(state, vote):
# # #     print(s, "vote is", v)      # Ogun vote is 12
# # #                                 # Oyo vote is 14
# # #                                 # Ondo vote is 15
# # # """you use the first letter of your argument"""
# # # # map()
# # # nums = [1, 2, 3, 4]
# # # squared = list(map(lambda x: x**2, nums))
# # # print(squared)  # [1, 4, 9, 16]

# # # # filter ()
# # # even_nums = list(filter(lambda x: x % 2 == 0, nums))
# # # print(even_nums)        # [2, 4]
# # # odd_nums = list(filter(lambda x: x % 3 == 0, nums))
# # # print(odd_nums)     # [3]

# # # # Step 1
# # # name1 = input("Enter first student name: ")
# # # score1 = int(input("Enter score for " + name1 + ": "))

# # # name2 = input("Enter second student name: ")
# # # score2 = int(input("Enter score for " + name2 + ": "))

# # # name3 = input("Enter third student name: ")
# # # score3 = int(input("Enter score for " + name3 + ": "))

# # # # Step 2: store in lists
# # # names = [name1, name2, name3]
# # # scores = [score1, score2, score3]

# # # # Step 3: Display data
# # # print("\nStudent Data:")
# # # for index, (n, s) in enumerate(zip(names, scores)):
# # #     print(f"{index + 1}. {n} - {s}")    # Student Data:
# # #                                         # 1. Sam - 12
# # #                                         # 2. Ken - 10
# # #                                         # 3. Mabel - 9
# # # # state = ["Ogun", "Oyo", "Ondo"]
# # # # vote = [12, 14, 15]
# # # # for index, (s, v) in enumerate(zip(state, vote)):
# # # #     print(f"{index + 1}. {s} - {v}")    # 1. Ogun - 12
# # # #                                         # 2. Oyo - 14
# # # #                                         # 3. Ondo - 15

# # # # Step 4: Summary using built-ins
# # # total = sum(scores)
# # # average = round(total / len(scores), 2)
# # # highest = max(scores)
# # # lowest = min(scores)

# # # print("\nPerformance Summary:")     # Performance Summary:
# # # print("Total score:", total)        # Total score: 31
# # # print("Average score:", average)    # Average score: 10.33
# # # print("Highest score:", highest)    # Highest score: 12
# # # print("Lowest score:", lowest)      # Lowest score: 9

# # # # Step 5: Ranking (using sorted and zip)
# # # ranked = sorted(zip(scores, names), reverse=True)
# # # print("\nRanking:")
# # # for rank, (score, name) in enumerate(ranked, 1):
# # #     print(f"{rank}. {name} - {score}")  # Ranking:
# # #                                         # 1. Sam - 12
# # #                                         # 2. Ken - 10
# # #                                         # 3. Mabel - 9
# # # # Step 6: Check data types
# # # print("\nData Type Checks;")            # Data Type Checks;
# # # print("Type of names:", type(names))    # Type of names: <class 'list'>
# # # print("Type of scores:", type(scores))  # Type of scores: <class 'list'>
# # # print("ID of names list:", id(names))   # ID of names list: 2920776958464
# # # print("ID of scores;", id(scores))      # ID of scores; 2920774459584

# # # # Step 7: Filter passing students (>=50)
# # # passing = list(filter(lambda s: s >= 50, scores))
# # # print("\nPassing Scores:", passing)     # Passing Scores: []

# # # # Step 8: Map names to uppercase
# # # upper_names = list(map(lambda n: n.upper(), names))
# # # print("Uppercase names:", upper_names)  # Uppercase names: ['SAM', 'KEN', 'MABEL']

# # # lower_names = list(map(lambda n: n.lower(), names))
# # # print("Lowercase names:", lower_names) # Lowercase names: ['sam', 'ken', 'mabel']

# # # # Step 9: Use help() to show documentation of len
# # # print("\nHelp on len():")
# # # help(names)

# # # Defining a function
# # # def greet():
# # #     print("Hello, welcome to AI Fellowship!")


# # # greet()              # Hello, welcome to AI Fellowship!   
# # # greet()              # Hello, welcome to AI Fellowship!

# # # # Function with an argument - the placeholder
# # # def greet(name):
# # #     print("Hello", name,","  " welcome")

# # # greet("Class rep")                  # Hello Class rep , welcome
# # # greet("Ore")                        # Hello Ore, welcome

# # # def greet(name):
# # #     print("Hello", name)

# # # result = greet("Ore")               # Hello Ore 
# # # print("Result:", result)            # Result: None

# # # def add(a, b):
# # #     return a + b
# # # result = add(4, 6)
# # # print("The sum is:", result)        # 10

# # # def add(a, b):
# # #     return a + b
# # # result = add("c", "f")
# # # print(result)               #cf

# # # def add(a, d):
# # #     return a + d
# # # result = add("e", "f")
# # # print(result)           #ef

# # # def count_up_to(n):
# # #     i = 1
# # #     while i <=n:
# # #         yield i
# # #         i += 1
# # # for number in count_up_to(5):
# # #     print(number)       # 1
# # #                         # 2
# # #                         # 3
# # #                         # 4
# # #                         # 5

# # # def count_up_to(n):
# # #     i = 2
# # #     while i <=n:
# # #         yield i
# # #         i += 2
# # # for number in count_up_to(5):
# # #     print(number)       # 2
# # #                         # 4
# # # def introduce(name, track):
# # #     print("My name is", name)   # My name is Ngozi
# # #     print("I am learning", track, ".") # I am learning AI Engineering.
# # # introduce("Ngozi", "AI Engineering")
# # # introduce("Ai Engineering", "Ngozi")    # My name is Ai Engineering
# #                                         # I am learning Ngozi .
# # # def introduce(name, track):
# # #     print("My name is", name)       # My name is Ngozi
# # #     print("I am learning", track,".") # I am learning AI Engineering .
# # # introduce(name = "Ngozi", track = "AI Engineering")
# # # introduce(track = "AI Engineering",name = "Ngozi") # No changes made

# # # def introduce(name, track = "AI Engineering"):
# # #     print("My name is", name)       # My name is Paul
# # #     print("I am learning", track,".")   # I am learning AI Engineering .

# # # introduce("Paul") 

# # # def introduce(track, name = "Dan"):
# # #     print("My name is", name)
# # #     print("I am learning", track,".")
# # # introduce("AI Engineering")

# # # def add_numbers(*args):
# # #     total = 0
# # #     for num in args:
# # #         total += num
# # #     print("Sum:", total)
# # # add_numbers(2, 4, 6)                # Sum: 12
# # # add_numbers(10, 20, 30, 40, 50)     # Sum: 150

# # # def add_numbers(*ram):
# # #     total = 2
# # #     for t in ram:
# # #         total += t
# # #     print("Sum:", total)
# # # add_numbers(2, 4, 6)            # Sum: 14


# # # def student_details(**kwargs):
# # #     for key, value in kwargs.items():
# # #         print(key, ":", value)
# # # student_details(name="Peter", track = "AI Engineering", interests = "Block chain")
# # #     # name : Peter
# # #     # track : AI Engineering
# # #     # interests : Block chain

# # # def student_details(**note):
# # #     for key, value in note.items():
# # #         print(key, "--", value)
# # # student_details(name="Peter", track = "AI Engineering", interests = "Block chain")
# # #         # name -- Peter
# # #         # track -- AI Engineering
# # #         # interests -- Block chain
# # def participant_profile(name, age, track="AI Development", *skills, **extra_info):
# #     """
# #     Generate a profile for a bootcamp participant using different typees of arguments. 
# #     """
# #     profile = f"\n--- Bootcamp Participant Profile ---\n"
# #     profile += f"Name: {name}\n"
# #     profile += f"Age: {age}\n"
# #     profile += f"Track: {track}\n"

# #     #  Skills (from *args)
# #     if skills:
# #         profile += "Skills: " + ", ".join(skills) + "\n"
# #     else:
# #         profile += "Skills: Not yet specified\n"
    
# #     # Extra info (from **kwargs)
# #     if extra_info:
# #         profile += "Additional Info:\n"
# #         for key, value in extra_info.items():
# #             profile += f" - {key.capitalize()}: {value}\n"

# #     return profile
# # # Using positional arguments
# # print(participant_profile("Peter", 24)) # --- Bootcamp Participant Profile ---
# #                                         # Name: Peter
# #                                         # Age: 24
# #                                         # Track: AI Development
# #                                         # Skills: Not yet specified
# # # Adding keyword
# # print(participant_profile("Ore", 28, track="AI Engineering"))   #--- Bootcamp Participant Profile ---
# #                                                                 # Name: Ore
# #                                                                 # Age: 28
# #                                                                 # Track: AI Engineering
# #                                                                 # Skills: Not yet specified

# # # Adding variable-length positional arguments (*args)
# # print(participant_profile("Favour", 27, " Data Science", "Python", "SQL", 'Machine Learning'))
# # # --- Bootcamp Participant Profile ---
# # # Name: Favour
# # # Age: 27
# # # Track:  Data Science
# # # Skills: Python, SQL, Machine Learning

# # # Exam 4: Adding variable_length keyword arguments (**kwargs)
# # print(participant_profile(
# #     "Sophia", 30, "Cybersecurity",
# #     "Networking", "Ethical Hacking", "Python",
# #     interests="Blockchain", city="Shagamu", phone="0812345678"
# # ))

# # # --- Bootcamp Participant Profile ---
# # # Name: Sophia
# # # Age: 30
# # # Track: Cybersecurity
# # # Skills: Networking, Ethical Hacking, Python
# # # Additional Info:
# # #  - Interests: Blockchain
# # #  - City: Shagamu
# # # - Phone: 0812345678

# # Namespace
# # Global Namespace
# # employee = "General Employee"  

# # def IT_department():
# #     # Local Namespace inside IT_department
# #     employee = "Chris (IT)"
# #     print("Inside IT Department:", employee)

# # def Training_department():
# #     # Local Namespace inside Training_department
# #     employee = "Chris (Training)"
# #     print("Inside Training Department:", employee)

# # print("In Global Namespace:", employee)  # Refers to global variable

# # IT_department()   # Uses local variable in IT
# # Training_department()   # Uses local variable in Training

# # # Using a built-in namespace function
# # print("Length of 'Python':", len("Python")) 
  
# # #In Global Namespace: General Employee
# # #Inside IT Department: Chris (IT)
# # #Inside Training Department: Chris (Training)
# # #Length of 'Python': 6

# # worker = "General worker"

# # def Staff_depart():
# #     worker = "Ken Staff"
# #     print("Inside Staff depart:", worker)
# # def Non_staff():
# #     worker = "Ken Non_Staff"
# #     print("Inside Non_staff:", worker)
# # print("In Global Namespace:", worker)
# # Staff_depart()
# # Non_staff()

# # print("Length of 'worker':", len("Workers"))

# # x = "global x"  # Global namespace
# # def outer():
# #     x = "enclosing x"   # ENclosing namespace
# #     def inner():
# #         x = "local x"
# #         print("Inside inner:", x)   # Local wins
# #     inner()
# #     print("Inside outer:", x)   # Enclosing
# # outer()
# # print("In global:", x)
# # Inside inner: local x
# # Inside outer: enclosing x
# # In global: global x

# ### Global keyword
# x = 5
# def change_global():
#     global x
#     x = 15    # modifies the global x
# change_global()
# print(x)        # 15

# # non local keyword
# def outer():
#     x = "outer x"

#     def inner():
#         nonlocal x
#         x = "changed by inner"
#         print("Inside inner:", x)
#     inner()
#     print("Inside outer:", x)
# outer()
# # Inside inner: changed by inner
# # Inside outer: changed by inner

# def square(x):
#     return x ** 2
# # Lambda function
# square_lambda = lambda x: x ** 2
# print(square(5))            # 25
# print(square_lambda(5))        # 25

# add = lambda a, b: a + b
# print(add(3, 7))    # 10

# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)      # [1, 4, 9, 16]

# numbers = [10, 15, 20, 25, 30]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)        # [10, 20, 30]

students= [("Ayo", 20), ("Bola", 18), ("Chike", 22)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)
students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)
# [('Bola', 18), ('Ayo', 20), ('Chike', 22)]
# [('Chike', 22), ('Ayo', 20), ('Bola', 18)]
# [('Ayo', 20), ('Bola', 18), ('Chike', 22)]