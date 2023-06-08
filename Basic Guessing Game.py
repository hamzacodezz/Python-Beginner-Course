def basegame():
    secretword="giraffe"
    guess=""
    isright=False
    tries=0
    triesleft=3
    while guess!=secretword:
        guess=input("What is the secret word? Have a guess: ")
        guess=guess.lower()
        tries+=1
        triesleft-=1
        if guess!=secretword:
            if tries==3:
                print("You have ran out of tries! You lose")
                break 
            else:
                print("Wrong!You have "+str(triesleft)+" tries remaining!")
        else:
            print("You Win!")
def playagain():
    again=input("Do you want to play again? Yes or no: ")
    if again.lower()=="yes":
        main()
    elif again.lower()=="no":
        print("Until next time!")
    else:
        print("Invalid input, try again.")
        playagain()

def main():
    basegame()
    playagain()

main()