#2d arrays - lists within lists
numbergrid=[
    [1,2,3],#Essentially a grid    
    [4,5,6],
    [7,8,9],
    [0]
]
print(numbergrid)
print(numbergrid[0][2])#How to access elements

#Nested for loops - for loops within for loops

for row in numbergrid:
    for col in row:
        print (col)