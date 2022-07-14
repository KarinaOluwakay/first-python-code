# print("Hello World")
# print("Hello World\n"+" My name is Angel\n" +" I am 13 years old\n "+ "I want to study science in he university" )
# print("Oh sing"*-5)

# name = "Christopher"
# print(len(name))

question_answer = input("""
    Q1.Which animal has four stomach compartment?
    a - cow
    b - pig
    c - goat\n>_
    """).lower()

if question_answer == "c": 
    print("correct")
elif question_answer == "a" or question_answer == "b":
    print("wrong")
else:
    print("You did not choose any of the given options")

distance_to_convert = int(input("Input the distance to convert in metres \n>_"))
menu_chioce = input("""
Pick an option below to convert distance
pick :
km - Kilometre
cm - Centimetre
dm - Decimetre
m - Miles

""").lower()

distance_in_cm = distance_to_convert * 100
print(f"The distance{distance_in_cm}m in cm is{distance_in_cm}cm")

