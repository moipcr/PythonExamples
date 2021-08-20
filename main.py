# This is a sample Python script.

def print_primeNumber():
    for i in range(0,10):
        for n in range (2,i):
            if (i % n == 0):
                print(i,"equals:" , n, '*',i//n)
                break
        else:
            print(i, "is a prime" )


def printPyramid():
    height = int(input("Elige una altura: \n"))

    for y in range(0, height):
        for z in range(height,y,-1 ):
            print(end=" ")
        for x in range(y+1):
            print("* ",end='')
        else:
            print()





if __name__ == '__main__':
    printPyramid()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
