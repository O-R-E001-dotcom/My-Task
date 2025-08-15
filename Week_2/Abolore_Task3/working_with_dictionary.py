
#Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)  # {'name': 'Ada', 'age': 20, 'course': 'Computer Science'}

list = {
    "height": 24.6,
    "name": "Uju",
    "race": "latino"
}
print(list) # {'height': 24.6, 'name': 'Uju', 'race': 'latino'}

# Using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info) #{'name': 'John', 'age': 25, 'course': 'Maths'}

list = dict(height=24.6, name="Uju", race="latino")
print(list) # {'height': 24.6, 'name': 'Uju', 'race': 'latino'}

# Empty dictionary
empty_dict = {}
print(empty_dict)   # {}

list = {}
print(list)

#c Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}  
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

square = {x: x**3 for x in range(1, 6)}
print(square)   # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)   #{2: 8, 4: 64, 6: 216, 8: 512}

odds_cube = {x: x**3 for x in range(1, 10) if x % 3 == 0}
print(odds_cube)    # {3: 27, 6: 216, 9: 729}

#From existing dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)

passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)  # {'Ada': 85, 'Musa': 65}

students = {"Uju": 30, "Yamal": 36, "Kabal": 49}
failed_students = {name: score for name, score in students.items() if score <= 40}
print(failed_students)  # {'Uju': 30, 'Yamal': 36}

# Using String Keys

names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)  #{'Ada': 3, 'John': 4, 'Musa': 4} 

items = ["Yam", "Beans", "Bread", "tea"]
lengths = {item: len(item) for item in items}
print(lengths)  # {'Yam': 3, 'Beans': 5, 'Bread': 5, 'tea': 3}

# # Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
print(student["name"])  # Ada
print(student["course"])    # Computer science 
print(student.get("age"))   # 29

# Change value
student["age"] = 21
# Add new value
student["grade"] = "A"

print(student) #{'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

student["race"] = "latino"
print(student) #{'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'grade': 'A', 'race': 'latino'}

# Using pop() to remove
student.pop("grade")
print(student) # {'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'race': 'latino'}

# Using popitem() - removes last inserted key-value
student.popitem()
print(student) # {'name': 'Ada', 'age': 21, 'course': 'Computer Science'} # it removed race

# Using del keyword
del student["course"]
print(student) # {'name': 'Ada', 'age': 21} it removed course
# Using clear() - removes all items
student.clear()
print(student)      # {}

# Dictionary Methods
person = {"name": "Emeka", "age": 30}

# 1. keys()
print(person.keys())    # dict_keys(['name', 'age'])
# 2. values()
print(person.values())  # dict_values(['Emeka', 30])
#3. items()
print(person.items())   # dict_items([('name', 'Emeka'), ('age', 30)])
# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)   # {'name': 'Emeka', 'age': 31, 'city': 'Lagos'}
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
 #Loop through keys
for key in student:
    print(key)  #name
                #age
                #course
#Loop through values
for value in student.values():
    print(value)        # Ada
                        # 20
                        # Comnputer science
# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Storing a student's biodata
student = {
    "name": "Adanna",
    "age": 20,
    "subjects": ["Maths", "Eng", "Chem"],
    "is_full_time": True
}
print(f"Name: {student['name']}")           # Name: Adanna
print(f"subjects: {', '.join(student['subjects'])}")    # Subjects: Maths, Eng, Chem