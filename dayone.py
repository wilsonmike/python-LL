# print("Hello, " + input("What is your name? "))
# name = input("What is your favorite programming language? ")
# print(name)

# day one username generator

    # city = input("What's the name of the city you grew up in?\n")
    # pet = input("What's your pet's name?\n")
    # print("Your username could be " + city + " " + pet)

#day two tip calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are going to split the bill? "))
bill_with_tip = tip / 100 * total_bill + total_bill
total_bill = bill_with_tip / people
round(total_bill, 2)
print(f"Each person should pay {total_bill}")

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

