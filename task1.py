print()
print("Welcome to PyWorkshop")
print("Are you beginner in Python?")

# GET CREATIVE:
# Ask your player a second question and use the answer.

answer = input("")

if answer == "yes":
    print("You're on the right meetup!")
    print("What is your goal?")
    print("1.Get a feeling of programming")
    print("2.Become a Python developer")

    answer2 = input("1 or 2?")

    if answer2 == "1":
        print("You will definitely have the feeling of programming after this meetup")
    elif answer2 == "2":
        print("Well, this will take a while but it's your first step, way to go!") 

elif answer == "no":

    print("Normally you shouldn't be here, but let me ask you one thing")
    print("Are you a Python coach?")

    answer3 = input("yes/no")

        if answer3 =="yes":
            print("Ooh, all good then, you're very welcome here")
            print("Thanks for being and helping here today!") 

        elif answer3 =="no":
        print("Hm, maybe you should't be here :) ")
        print("This course is for complete beginners")
        print("Do you want to search for another Meetup that is more suitable for you?")

        answer4 = input("")

        if answer4 == "yes":
            print("You will be redirected to the Meetup homepage shortly")
        else:
            print("Was nice to meet you, Bye!")

        else: 
        print("What brought you here then?") 
        input("")  

else:
    print("Please reply 'yes' or 'no'")