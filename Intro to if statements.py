ismale=True
istall=False
if ismale and istall:
    print ("You are a tall male")
elif ismale  and not(istall):
    print("you are not tall")
elif not(ismale) and istall:
    print("you are not a male")
else:
    print("You are not a tall male")