#make a list and store a "sentence" "action" "place/thing"

subjects = [
    "Roman reigns",
    "Hardik pandya",
    "Lion king" ,
    "A group of boy",
    "Car driver",

]

actions = [
    "work ",
    "fight with oppenent",
    "play a cricket",
    "reads a book",
    "cooks"
]

places_things =  [
    "in the kitchen.",
    "at my desk.",
    "in the library.",
    "in the park.",
    "in the ring.",
    "at the boundry.",
]
#making loop 
import random
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(places_things)

    headline = f"BREKING NEWS: {subject} {action} {place_thing}"
    print("\n"+ headline)
     
    user_input = input("Do you want to another headline ?(yes/no):" ).strip()
    if user_input == "no":
        break

#printing goodby masege
print("Thanks to use fake headline ganerator:")
