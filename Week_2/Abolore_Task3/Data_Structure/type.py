# # Using square brackets
# # empty_list = []
# # print(empty_list)   # Output: []
# # brain = []
# # print(brain)    #output: []
# # #Using the list() constructor
# # empty_list2 = list()
# # print(empty_list2)  #[]
# # brain2 = list()
# # print(brain2)   #[]
# # #List of integers
# # numbers = [1, 2, 3, 4, 5]
# # print(numbers)  # [1, 2, 3, 4, 5]

# # num = [2, 4, 6]
# # print(num)  # [2, 4, 6]
# # #List of strings
# # fruits = ["apple", "banana", "cherry"]
# # print(fruits)   #['apple', 'banana', 'cherry']

# # egg = ("apple", "banana")
# # print(egg)  #('apple', 'banana')

# # Mixed data types
# # mixed_list = ["Alice", 25, 5.8, True]
# # print(mixed_list)  # ['Alice', 25, 5.8, True]

# # # From a string (each character becomnes an element)
# # chars = list("hello")
# # print(chars)    # ['h', 'e', 'l', 'l', 'o']

# rat = list["hello"]
# print(rat)  # list['hello']

# # Tuple
# # my_tuple = (10,20,30)
# # list_from_tuple = list(my_tuple)
# # print(list_from_tuple)  # [10, 20, 30]

# # mine = (b,c)
# # text = list(mine)
# # print(text) 

# # # From range
# numbers_range = list(range(5))
# print(numbers_range)    # [0, 1, 2, 3, 4]
# numbers_range = list(range(8))
# print(numbers_range)    # [0, 1, 2, 3, 4, 5, 6, 7]
# letters_range = list(range(8))
# print(letters_range)    # [0, 1, 2, 3, 4, 5, 6, 7]

# # Squares of numbers 0-4
# squares = [x**2 for x in range(5)]
# print(squares)  #[0, 1, 4, 9, 16]
# squares = [6**2]
# print(squares) # 36
# squares = [6*1*1**2]
# print(squares) #6 seems ** after didnt work

# Even numbers between 0-10
# evens = [x for x in range(11) if x % 2 == 0]
# print(evens)    #[0, 2, 4, 6, 8, 10]
# odds = [x for x in range(11) if x % 3 == 0]
# print(odds) #[0, 3, 6, 9]
# odds = [x for x in range(11) if x % 3]
# print(odds) #[1, 2, 4, 5, 7, 8, 10] numbers dat 3 can divide aren't included
# odds = [x for x in range(11) if x % 3 == 2]
# print(odds) # [2, 5, 8]
# evens = [x for x in range(11) if x % 3 == 0]
# print(evens)    # [0, 3, 6, 9]

# Matrix-like list
# matrix = [[1, 2], [3, 4], [5, 6]]
# print(matrix)   # [[1, 2], [3, 4], [5, 6]]
# print(matrix[0])     # Output: [1, 2]
# print(matrix[0][1])  # Output: 2
# print(matrix[2][1]) # 6
# print(matrix[0][0][1])  #not subscriptable

# matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
# print(matrix[0][1][2])  #not subscriptable
# fruits = ["mango", "orange", "banana"]
# print(fruits[1])    # orange (second element)
# print(fruits[0][1]) #a beacuse it is quoted

# fruits = ["mango, orange, banana, yam"]
# print(fruits[0][1]) # a (it is quoted and a is no. 1)

# fruits = [["yam", "rice"], ["orange", "tea"]]
# print(fruits)   # [['yam', 'rice'], ['orange', 'tea']]
# print(fruits[0][1])     #rice

# names = ["Bam"]
# names.append("Lara")
# names.append("George")
# print(names)   # ['Bam', 'Lara', 'George']


# List operations
# num1 = [1, 2, 3]
# num2 = [4, 5]
# result = num1 + num2
# print(result)   #[1, 2, 3, 4, 5]

# Repetition 
# nums = [1, 5]
# repeated = nums * 4
# print(repeated) #[1, 5, 1, 5, 1, 5, 1, 5]

# Indexing
# food = ["yam", "rice", "noodles"]
# print(food[0])  #yam
# print(food[-1]) #noodles
# print(food[-2]) #yam

# Slicing
nums = [3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])    #[5, 6, 7]
print(nums[:2]) #[3,4]
print(nums[5:])  # 8, 9
print(nums[:5]) # [3, 4, 5, 6, 7]

# nums = [3, 5, 7, 8, 4, 2]
# print(nums[:3])     #3, 5, 7
# print(nums[::2])    #3,7,4
# print(nums[::3])    #[3, 8]