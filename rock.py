import random
def play():
    print("let's play the play the rock-paper-scissors game")
    while True:
        user=int(input("enter ur choice for rock 0,paper 1,scissors 2:"))
        if(user>=3 or user<0):
            print("invalid")
        else:
            com=random.randint(0,2)
            print("computer choice:",com)
            if(com==user):
                print("it's a draw")
            elif((user==2 and com==1) or (user==0 and com==2) or (user==1 and com==0) ):
                print("user wins!")
            else:
                print("user lose!")
            play_again=input("do u want to play again?(yes/no):").lower()
            if play_again=="no":
                print("go to home!")
                break
play()
