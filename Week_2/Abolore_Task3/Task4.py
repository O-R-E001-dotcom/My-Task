
# TASK 1
Quote = input("fav quote: ")  #god is good
Quote_title= Quote.title()
print("\"" + Quote_title + "\"")            # "God Is Good"

# TASK 2
Empty_list = []
for items in range (3):
    Options = input(f"shopping list {items+1}: ")
    Empty_list.append(Options)
    print(" , ".join(Empty_list))


empty_list = []
Item1 = input("item1: ")    # Egg
Item2 = input("item2: ")    # Tea
Item3 = input("item3: ")    # Bread
empty_list.append(Item1)
empty_list.append(Item2)
empty_list.append(Item3)
print(",".join(empty_list)) # Egg, tea, bread

# Task 3
user = input("sentence: ")  #I am me
print(user.split())     # ['I', 'am', 'me']
print(len(user))        # 7 together with the space

# Task 4
names = []
for name in range (5):
    all_names = input(f"Enter the names here {name+1}: ".lower())
    names.append(all_names)
names.sort()
print("\n".join(names))         #ada #bim # lara #seun # yemi

# Task 5
names = []
scores = []
name1 = input("name1: ")        # Ada
name2 = input("name2: ")        # Uju
name3 = input("name3: ")        # Lara
score1 = input("score1: ")      # 32
score2 = input("score2: ")      # 23
score3 = input("score3: ")      # 43
names.append(name1)
names.append(name2)
names.append(name3)
scores.append(score1)
scores.append(score2)
scores.append(score3)
result = (f"{names}\n{scores}")
print("-".join(result))
result = list(f"{name1}\t{score1}\n{name2}-\t{score2}\n{name3}\t{score3}".split())
print(result)

# Task 6
user = input("word: ")      # I hope it is worth it
print(len(user))            # 21
# To check
print(user.isupper())       # False
print(user.islower())       # False
print(user.istitle())       # False
# Reverse the word
print(user[::-1])           # ti htrow si ti epoh I

# Task 7

