# User to input a word
user = input("Enter a word: ")      # I think So
print(len(user))        # 10
# Printing length of the word using len()
if user.isupper():
    print("The letters are in uppercase")   
elif user.islower():
        print("In lower case")
elif user.istitle():
      print("They are in title case")
else:
      print("Unknown")      # 10
                            # Unknown
                            # oS kniht I

# # Checking if it is all uppercase, lowercase, or titlecase
# print(user.islower())   # False
# print(user.isupper())   # False
# print(user.istitle())   # False
# Reversing using slicing
print(user[::-1])