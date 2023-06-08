def hungerlevel():
    hunger = input("Are you hungry? Yes or No: ")
    hunger = hunger.upper()
    if hunger=="YES":
        print("You eat breakfast")
    elif hunger=="NO":
        print("You Skip breakfast")
    else:
        print("Invalid input")
        hungerlevel()
def cloudy():
    cloud=input("Is it cloudy? Yes or No: ")
    cloud = cloud.upper()
    if cloud=="YES":
        print("You take your umbrella")
    elif cloud=="NO":
        print("You take Sunglasses")
    else:
        print("Invalid input")
        cloudy()
def resturant():
    meat=input("Do you want meat? Yes or No: ")
    meat = meat.upper()
    if meat=="YES":
        print("Order a steak")
    elif meat=="NO":
        pastaorder()
    else:
        print("Invalid input")
        resturant()
def pastaorder():
    pasta=input("Do you want pasta? Yes or No: ")
    pasta = pasta.upper()
    if pasta=="YES":
        print("Order Spagetti meatballs")
    elif pasta=="NO":
        print("Order salad")
    else:
        print("Invalid input")
        pastaorder()

def main():
    print("You wake up")
    hungerlevel()
    print("You leave your house. ")
    cloudy()
    print("You go to the resturant")
    resturant()

main()