# Program is syntactically correct, but an error occurs while running
# Also called exceptions
# a. 

# User to input a word
try:
        user = str(input("Enter the word (I think So):"))      # I think So

        print(len(user))        # 10
            # Printing length of the word using len()
        if user.isupper():
                print("The letters are in uppercase")   
        elif user.islower():
                    print("In lower case")
        elif user.istitle():
                print("They are in title case")
        else:
                print("Not all in upper, lower or title case")  
except:
    print("Error occurred")