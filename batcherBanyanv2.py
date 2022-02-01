#used for random number
import random

#Banyon network is performed in the funcitons below
def firstColumn(input, dst):
    if input == 'a1' or 'a3':
        if dst[0]=='0':
            path2 = 'b1'
        else:
            path2 = 'b3'
    if input == 'a2' or 'a4':
        if dst[0]=='0':
            path2 = 'b2'
        else:
            path2 = 'b4'
    return path2
def middleColumn(input, dst):
    if input == 'b1' or 'b2':
        if dst[1]=='0':
            path3 = 'c1'
        else:
            path3 = 'c2'
    if input == 'b3' or 'b4':
        if dst[1]=='0':
            path3 = 'c3'
        else:
            path3 = 'c4'
    return path3
def lastColumn(input, dst):
    if input == 'c1':
        if dst[2]=='0':
            path4 = '0'
        else:
            path4 = '1'
    if input == 'c2':
        if dst[2]=='0':
            path4 = '2'
        else:
            path4 = '3'
    if input == 'c3':
        if dst[2]=='0':
            path4 = '4'
        else:
            path4 = '5'
    if input == 'c4':
        if dst[2]=='0':
            path4 = '6'
        else:
            path4 = '7'
    return path4

#taking input from user and performing Batcher sorting in the function below
def main():
    numberVal = []
    n= int(input("Please enter number of inputs for the random number generator: "))
    for i in range(n):
        rando = random.randint(0, 7)
        while rando in numberVal:
            rando = random.randint(0, 7)
        numberVal.append(rando)
    print("The random numbers are: ", numberVal)
    numberVal.sort()
    dictionary = {}
    for i in range(n):
        dictionary[i] = numberVal[i]
    print("After Batcher sorting, the numbers are: ", dictionary)
    starting_points = {'0': 'a1', '1': 'a2', '2': 'a3', '3':'a4', '4': 'a1', '5':'a2', '6': 'a3', '7': 'a4'}
    for i in range(n):
        x = bin(dictionary[i])[2:].zfill(3)
        path1 = starting_points[str(i)]
        path2 = firstColumn(path1, x)
        path3 = middleColumn(path2, x)
        path4 = lastColumn(path3, x)
        print("Path for port "+str(i)+" to output "+str(dictionary[i])+" is"+" " + path1 + " --> "+" "+path2+" --> "+" "+path3+" --> "+" "+path4)
if __name__ == '__main__':
    main()

