#  loops

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

# for each 
# for number in numbers:
#     if number >= 0:
#         positive_number_count += 1
#         print(number)

# print(positive_number_count)

########################################### 

# for loop
# for i in range(5):
#     if i>=0:
#         print("Positive")
#     else:
#         print("Negative")   

########################################### 

# sum of even  number
# num = int(input("Enter a number: "))
# sum_even = 0;

# for i in range(1, num+1):
#     if i%2 == 0:
#         sum_even += i
       
# print("Sum of even numbers:", sum_even)

########################################### 

# mutiplication table -- IMPORTANT
# mul = int(input("Enter  number: "))

# for i in range(1, 11):
    
    # if (i != 5):
    #     print(f"{mul} x {i} = {mul*i}")   
    # else:
    #     continue

    #  if (i != 5):
    #     print(f"{mul} x {i} = {mul*i}") 
    #     continue

    # if (i == 5):
    #     continue
    #     print(f"{mul} x {i} = {mul*i}") 

    # if (i == 5):
    #     continue
    # print(f"{mul} x {i} = {mul*i}") 

    #  if (i != 5):
    #     continue    ### equivalent to SKIP this condition and move to next iteration
    #  print(f"{mul} x {i} = {mul*i}") 
        
########################################### 

#  reverse string
# str = input("Enter a string: ")

# reversed_str = ""

# # length = len(str)+1;
# # for i in range(-1, -length, -1):
# #     reversed_str += str[i]   

# for i in str:
#     reversed_str = i + reversed_str

# print(reversed_str)    

########################################### 

#  Find first non-repeating character in a string
# str = input("Enter a string: ")

# for char in str:
#     if str.count(char) == 1:
#         print("First non-repeating character is:", char)
#         break

############################################

# factorial of a number

# num = int(input("Enter a number: "))

# for i in range(1, num):
#     num *= i


# factorial = 1
# while num>0:
#     factorial *= num
#     num -= 1   

# print("Factorial is", factorial)

#################

# prime number

# num = int(input("Enter a number: "))

# is_prime = True

# for i in range(2, num):
#     if num % i == 0:        
#         is_prime = False
#         break

# print("Is prime?", is_prime)


##################################

# find duplicate in a list

# items = ["apple", "banana", "kiwi", "orange", "grape", "apple", "kiwi"]

# unique_items = set() # distinct bucket to store unique items

# for i in items:
#     if items.count(i) > 1:
#         print("Duplicate item is:", i)
#         break

# for i in items:
#     if i in unique_items:
#         print("Duplicate item is:", i)
#         break
#     else:
#         unique_items.add(i)

############################

# Sorting a list of lists/tuples by the second element 
# - key= → Python asks: “What value should I use to compare items?”
# - lambda x: → defines a tiny anonymous function that takes one argument (x)
# - x[1] → returns the second element of that item

a = [(1, 3), (4, 1), (2, 2)]
sorted_list = sorted(a, key=lambda x: x[1])

# Sort in descending order
# sorted_list = sorted(a, key=lambda x: x[1], reverse=True)

# Using .sort() to sort in place

a.sort(key=lambda x: x[1])
print(sorted_list)

############################


# Sorting a dict 
# a = [{"name": "A", "score": 10},
#      {"name": "B", "score": 5},
#      {"name": "C", "score": 8}]

# sorted_list = sorted(a, key=lambda x: x["score"])
# print(sorted_list)


##############################

# ENUMERATE

# a = [0,5,2] # it can be list/set/tuple
# enumerate(a) creates an enumerate object, but it does not convert it to a list or print anything.
# so you have wrap it up with list or set or list 

# print(list(enumerate(a))) # [(0,0), (1,5), (2,2)]
# print(set(enumerate(a)) ) # {(0,0), (1,5), (2,2)}
# print(tuple(enumerate(a))) # ((0,0), (1,5), (2,2))


