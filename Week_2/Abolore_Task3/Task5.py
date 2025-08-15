# Task 1
# Input user's fav Nigerian dishes
dish_1 = input("first dish: ")      # Broccoli
dish_2 = input("second dish: ")     # Beans
dish_3 = input("third dish: ")      # Rice
dishes = (dish_1, dish_2, dish_3)
# Storing them in a tuple called dishes
dishes_tuple = tuple((dishes))  # ('broccoli', 'beans', 'rice')
# Printing the tuple in a single line
print(dishes_tuple)
# Printing using \n escape sequence
print("\n".join(dishes_tuple))

# Task 2
# Input 5 best firend's names with split()
User = input("5 best friend's names: ").split() # Sola, Lara, Tayo, Louis, Ray
# Storing them in a tuple called friends
Friends_tuple = tuple(User)
# Printing in reverse order
print(Friends_tuple[::-1])  # ('Ray', 'Louis,', 'Tayo,', 'Lara,', 'Sola,')

# Task 3
name_of_states = ("Lagos", "Abia", "Oyo", "Ondo", "Bauchi")
# Printing the first state and last state using membership
print("Lagos" in name_of_states)        # True
print("Bauchi" in name_of_states)       # True
# Print the number of states
print(len(name_of_states))              # 5

# Task 4
# Asking for user's info
user = {"first_name": "Obi", "age": 23, "fav_color": "blue","hometown": "Abeokuta"}
# Storing in a tuple profile
profile_tuple = tuple(user)
# Unpacking into variables
for key, value in user.items():
    print(f"{key}: {value}")    # first_name: Obi
                                # age: 23
                                # fav_color: blue
                                # hometown: Abeokuta
# Printing using escape sequence
print("First_name  \tObi    \nAge       \t23    \nFav_color \tBlue  \nHometown  \tAbeokuta")


# Task 5
item1 = input("enter item1:")       # Perfume
item2 = input("enter item2: ")      # Moist
item3 = input("enter item3: ")      # Mist
shopping_list = (item1, item2, item3)
# Storing in tuple shopping_list
shopping_list_tuple = tuple(shopping_list) 
# Converting to a list, and adding two more items
lists = list(shopping_list_tuple) 
lists.append("rice")
lists.append("egg")

# Converting back to a tuple
updated_list = tuple(lists)
print("|".join(updated_list))   # Perfume|moist|mist|rice|egg

# Task 6

