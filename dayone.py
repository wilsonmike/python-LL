# print("Hello, " + input("What is your name? "))
# name = input("What is your favorite programming language? ")
# print(name)

# day one username generator

    # city = input("What's the name of the city you grew up in?\n")
    # pet = input("What's your pet's name?\n")
    # print("Your username could be " + city + " " + pet)

#day two tip calculator

    # print("Welcome to the tip calculator")
    # total_bill = float(input("What was the total bill? $"))
    # tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    # people = int(input("How many people are going to split the bill? "))
    # bill_with_tip = tip / 100 * total_bill + total_bill
    # total_bill = bill_with_tip / people
    # round(total_bill, 2)
    # print(f"Each person should pay {total_bill}")

#fizzbuzz practice 

# for num in range(0,20):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# day 3 treasure console app
    # print("Welcome to the rollercoaster!")
    # height = int(input("What is your height in cm? "))
    # if height > 120:
    #     print("You are tall enough for the ride!")
    # else:
    #     print("Sorry you do not meet the height requirement for this ride =(")
        
    
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Find the treasure...")
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")