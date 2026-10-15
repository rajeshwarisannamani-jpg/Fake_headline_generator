#import the random module
import random
#create subjects
subjects=[
    "puneeth",
    "virat kohli",
    "A mumbai cat",
    "PM Modi",
    "siddramaiah",
    "rashmika mandhana",
    "cycle",
    "A group of monkeys"
]
actions=[
    "launches",
    "cancles",
    "Dances with",
    " declares war",
    "gandhiji reborn celebration",
    "eats",
]
places_or_things=[
    "At red fort",
    " in hubli local train",
    "beauty palour",
    "IPL match",
    "going to bailhongal",
    "chicken chilli"
]
#start headline generation loop
while True:
    subjects=random.choice(subjects)
    actions=random.choice(actions)
    places_or_things=random.choice(places_or_things)
    headline=f"BREAKING NEWS:{subjects} {actions} {places_or_things}"
    print("\n"+ headline)

    user_input=input("\n Do you want another headline?(yes/no):").strip()#extra spaces will remove 
    if user_input=="no":
        break
print("\nThanks for using fake headlines generator.Have a fun day!!")








