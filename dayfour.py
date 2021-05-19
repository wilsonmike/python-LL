import os
clear = lambda: os.system('cls')
# programming = ['React','Angular','C++','Python','Go']
# for items in programming:
#     print(items)
    

# for number in range(1,11,3):
#     print(number)

# password generator

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print('PyPassword Generator')
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like in your password?\n"))
# nr_numbers = int(input("How many numbers would you like in your password?\n"))

# #Ez solution
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
    
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
    
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#With randomization
# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
    
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))
    
# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))

# print(password)

#day 9 silent auction
    #dictionaries in python

programming_dictionary = {
    "Go" : "Really nice syntax, fast, and sick logo.",
    "React" : "Super in demand but frameworks are CRUD bound meh.",
    "Python" : "Becoming a tool for everything| ML, AI, and even the web. +1"
}
#retreiving items from dictionary
print(programming_dictionary["React"])

#adding new items to dictionary
programming_dictionary["C++"] = "Robust documentation, seems to be the leader in self driving vehicles."
print(programming_dictionary)

#actual day 9 project

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()