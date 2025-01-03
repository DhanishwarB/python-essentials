# print("Welcome To The Band Name Generator")
# city = input("which city did you grow up in?\n")
# pet = input("what is the name of your pet?\n")
# print("your band name could be :" + city + " " + pet)



# write me a code, where you should get a name from the user and print the message as "hello, user-name, have a good day!"
# user_name = input("what is your name : \n")
# print("hello " + user_name + " have a good day" )

# print(len("866812"))
# print(type("hello"))
# print(type(12345))
# print(type(345.675))
# print(type(True))
# print(type(False))
# print(3 * 3 + 3 / 3 - 3)
# bmi = 84 / 1.65 ** 2
# print(bmi)
#
# print(int(bmi))
# print(round(2.4))
# print(6 + 4 / 2 - (1 * 2))
# print("Welcome to the tip calculator")
# bill = float(input("what was the total bill $"))
# tip = int(input("what percentage tip would you like to give? 10 12 15"))
# people = int(input("how many people to split the bill?"))
# tip_as_percentage = tip / 100
# total_tip = bill * tip_as_percentage
# total_bill = bill + total_tip
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay :${final_amount}")
# print("welcome to the rollercoaster")
# height = int(input("your height in cm? "))
# bill = 0
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("what is your age? "))
#     if age <=12:
#         bill = 5
#         print("child tickets are $5")
#     elif age <=18:
#         bill = 7
#         print("youth tickets are $7")
#     elif age >=45 and age <=55:
#         print("age between this will have an free ride")
#     else:
#         bill = 12
#         print("adult tickets are $12")
#     wants_photo = input("do you want to have a photo take? Type y for Yes and n for No")
#     if wants_photo == "y":
#         bill += 3
#     else:
#         print(f"your final bill${bill}")
#
# else:
#     print("sorry you have to grow taller to ride the rollercoaster")


# number_to_check = int(input("what is the number you want to check? : "))
# if number_to_check % 2 == 0:
#     print("even")
# else:
#     print("odd")

# print("Welcome to python pizza deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("you've entered a wrong size")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
# print(f"your final bill$ {bill}")

# import random
# random_integer = random.randint(1, 40)
# print(random_integer)
# import random
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails ==0:
#     print("heads")
# else:
#     print("tails")


class_name = ["dhanish", 20, "male"]

print(class_name)
