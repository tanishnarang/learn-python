import time


hello="Hello there,"
print(hello.center(100))
time.sleep(1)

name="i am tanish"
print(name.center(100))
time.sleep(2)

welcome="I welcome you to my quiz game"
print(welcome.center(100))
time.sleep(3)

play=input("so would you like to play the game? ")
if play.lower() != "yes":
   quit()


time.sleep(2)
print("here you will get some questions \nand you will be scored out of 4 for it")


time.sleep(3)
print("\n\nhere is your first question")

score=0



time.sleep(1)
answer=input("what is my name? \nanswer:")
if answer.lower() == "tanish":
    print("correct")
    score += 1
else:
    print("incorrect")



time.sleep(1)
answer=input("\nwhat is my age? \nanswer:")
if answer == "19":
    print("correct")
    score += 1
else:
    print("incorrect")




time.sleep(1)
answer=input("\nwhat i am studying? \nanswer:")
if answer.lower() == "btech":
    print("correct")
    score += 1
else:
    print("incorrect")





time.sleep(1)
answer=input("\nwhat is my city's name? \nanswer:")
if answer.lower() == "fatehabad":
    print("correct")
    score += 1
else:
    print("incorrect")



print("\nyour score out of 4 is" , score)
print("your percentage is",(score/4)*100)









