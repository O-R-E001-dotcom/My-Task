# # a. Indentation error fixed
# for i in range(3):              # There was no tab space(indentation before "print")
#     print(i)        # 0
#                     # 1
#                     # 2

# # b. Missing colon/Parenthesis Error fixed
# if 5 > 3:          # It was missing colon
#     print("Hello")

# # c. Invalid Syntax - General grammar mistakes
# print("Hello")  # It was missing parentheses in python

while True: 
    ussd_code = input("Enter ussd code; *174#: ")      # *174#
    if ussd_code == "*174#":
       print("Welcome to my bank")
       break
    else:
        print("Invalid input. Please enter a number.")


balance = 75000
while True:
    
        print("\nMenu:")
        print("1. Check balance")
        print("2. Buy airtime")
        print("3. transfer")
        print("4. Buy data")
        print("5. Exit")

        try:
            option = input("Pick a number: ")
       
            if option  == "1":
                print(f"Your balance is: {balance}")
            elif option == "2":
                amount = int(input("Enter airtime amount: "))
                if amount <= balance:
                    balance -= amount
                    print(f"Recharge successful. New balance: {balance}")
                else:
                    print("Insufficient funds.")
            elif option == "3":
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    balance -= amount
                    print(f"Successful. New balance: {balance}")
                else:
                    print("Insufficient funds.")
            elif option == "4":
                amount = int(input("Enter data amount: "))
                if amount <= balance:
                    balance -= amount
                    print(f"Recharge successful. New balance: {balance}")
                else:
                    print("Insufficient funds.")
            elif option == "5":
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except:
            print("Not correct")
        finally:
            print("Closed")

        




