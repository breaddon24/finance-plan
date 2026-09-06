asterisks = "*" * 50

print(asterisks)
print()
print("*           THE LEGEND OF KHABEN FIBRE           *")
print()
print(asterisks)
print("*         Type 'Start' to Begin the Game!        *")
print(asterisks + "\n")

while True:
    start = input()         
    if start == "exit":
        exit()
    if start == "start" or "Start" or "START":
        break
while True:
    print()
    name = input("Hello there traveller! What is your name? ")
    if name == "exit":
        exit()
    if name.isalpha():
        print(f"""
        Hello there {name}! Its good meeting you! You see we will be venturing in a new world filled with many 
        different challenges and unknown possibilities, so get ready! This will be a journey worth dying for!
        """)
        break          
    else:
        print("Thats not a name. Use letters.")

while True:
    valid_age = input(f"To start how old are you {name}? ")
    try:
        if valid_age == "exit":
            exit()
        age = int(valid_age)
        if 13 <= age <= 100:
            print(f"I see, so you are {age} years old!")
            break
        elif 1 <= age <= 12:
            print(f"Sorry {name}, but you can't play just yet! Wait till you are a bit older young traveller!")
            exit()
        else:
            print("Enter a legit age.")           
    except ValueError:
        print("Please enter a number for your age.")

while True:
    print()
    gender = input("What is your gender? (Boy/Girl)")
    if gender == "exit":
        exit()
    if gender == "Boy" or gender == "boy":
        if 13 <= age <= 20:
            print("Nice to meet you young man!")
            break
        else:
            print("Nice to meet you good sir!")
            break

    elif gender == "Girl" or gender == "girl":
        if 13 <= age <= 20:
            print("Nice to meet you young lady!")
            break
        else:
            print("Nice to meet you madam!")
            break 
    else:
        print("That's not a gender, please try again.")

print(asterisks)
print(f"""
Well {name}, prepare for an amazing adventure, as we venture into the world of Monkeycity!
This is where everything fun and scary occurs, where you and me will go into unknown territory
and meet new friends along the way!
""")
print(asterisks)

while True:
    cont = input("Press Continue: ")

    if cont == "exit":
        exit()

    if cont == "continue" or cont == "CONTINUE" or cont == "Continue":
        break
print(asterisks)
print()

print(f"Buckle Up {name}! And welcome to The Legend of KHABEN FIBRE!!!")
