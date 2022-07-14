#  AMOUNT OF SWEET

# number_1 =int(input("Enter your first number"))
# number_2 =int(input("Enter your second number"))
# answer = number_1 - number_2
# print(answer)



# distance_in_m = int(input("Input the distance in meres\n>_"))
# distance_in_cm = distance_in_m * 100
# print(f"The distance {distance_in_m}m in cm is {distance_in_cm}cm")


# weather = input("What is the forcast for today?(hail/snow/sun/rain/cold)")
# if weather == "hail":
#     print("Remember your umbrella!")
# elif weather == "snow":
#     print("Remember your wooly gloves!")
# else:
#     print("Remember your sunglasses!")   
# if weather == "rain":
#     print("Remember your raincoat")
# elif weather =="cold":
#     print("Remember your coat")


#QUIZ
# answer = input("What is the capital of Dubia").lower()
# if answer == "abu dhabi":
#     print("you are correct")
# else:
#     print("you are wrong")


# question_answer = Input("""
#      Q1. In python, what do you call a box used to store data?
#      a - text
#      b - list
#      c - variable\n>_
# """).lower()

# if question_answer == "c":
#     print("correct")
# elif question_answer == "a" or question_answer == "b":
#     print("wrong")
# else:
#     print("You did not pick any of the given options")



#FROM THE DISTANCE CONVERTER PROJECT , USETHE MULTIWAY DECISION STATEMENTS
#TO CONVERT TO THE DISTANCE OF THE USERS'CHOICE



distance_to_convert  = int(input("Input the distance to convert in metres \n>_"))
menu_choice = input("""
Pick an option below to convert distance
pick : 
km - Kilometre
cm - Cenimetre
dm - decimetre
m - miles

""").lower()


distance_in_cm= distance_to_convert * 100
print(f"The distance {distance_in_cm}m in cm is {distance_in_cm} ")   



number_6 = input("Is number even?(y/n)")
if number_6 == "y":

 player_1 =int(input("Enter your first number"))
player_2 =int(input("Enter your second number"))
answer =player_1 + player_2 + 1
print =(answer)
