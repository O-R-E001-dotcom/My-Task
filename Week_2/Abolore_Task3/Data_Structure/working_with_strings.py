# Single quote
name = 'Ada'
print("Name: ", name)
# Double quote
greeting = "Hello"
print("Greeting: ", greeting)

 # Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada'''
print("Story: ", story)

# Strings with numbers and symbols
password = "p@ssw0rd123"
print("Password: ", password)

#Indexing
word = "Python"
print(word[3]) #h
print(word[-2]) #o

# Slicing
word = "Pythoned"
print(word[0:5])   # Pytho
print(word[2:])    # thoned
print(word[2::])    # thoned
print(word[:2])     #Py
print(word[:3])    # Pyt
print(word[::2])   # Ptoe
print(word[::3])  #Phe
print(word[::-1])   #ednohtyp
print(word[::-2]) #dnhy

# Concatenation
a = "Hello"
b = "World"
print(a + " " + b) # Hello World

# Repetition
word = "Hi!"
print(word * 3)     # Hi! Hi! Hi!

#Membership
text = "Python programming"
print("Python" in text)   # True
print("Java" not in text) # True

text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7

text = "Hello World"
print(text.index("World"))   # 6

filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True

# UPPER
name = "Ada Balogun"
print(name.upper())  
# Output: ADA BALOGUN

# lower
sentence = "python is amazing"
print(sentence.title())  
# Output: Python Is Amazing

text = "   Abuja   "
print(text.strip())  

fruits = "mango orange banana"
print(fruits.split())  
# Output: ['mango', 'orange', 'banana']
