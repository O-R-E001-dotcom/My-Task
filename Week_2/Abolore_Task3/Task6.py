# # User to input 5 fav fruits
# fruit1 = input("fav fruit 1: ")     # Banana
# fruit2 = input("fav fruit 2: ")     # Orange
# fruit3 = input("fav fruit 3: ")     # Kiwi
# fruit4 = input("fav fruit 4: ")     # Apple
# fruit5 = input("fav fruit 5: ")     # Cucumber
# all = set([fruit1, fruit2, fruit3, fruit4, fruit5])
# print(all)          # {'Banana', 'Orange', 'Kiwi', 'Apple', 'Cucumber'}

# # Task 2
# # Input the namees
# Names = set()
# # Adding names
# Names.add("Lara")
# Names.add("Seyi")
# Names.add("Uju")
# Names.sort()
# print("names:", Names)  # {'Lara', 'seyi', 'Uju'}

# # Task 3
# book  = set([x for x in range(1,51)])
# # Booking a seat number
# choose = int(input(" choose seat number: "))
# # Removing booked seat number
# book.remove(choose)
# # Printing remaining seats
# print(book)

# Task 4
users_name = {"Seyi", "Dotun"}
# Storing voter names in set
names = set(input("your names: "))
# Displaying warning if tried to registered twice
if names in users_name: 
    print("User already registered")
users_name.add("Uju")