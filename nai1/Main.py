import statistics
from math import sqrt
from nai1 import Flower


def getFlowerRowList(path):
    with open(path) as f:
        tList = f.readlines()

    return [x.rstrip() for x in tList]


def getFlowerDoneList(tList):
    trainFlowersList = []
    for i in tList:
        tData = i.split(",")
        trainFlowersList.append(Flower.Flower([float(i) for i in tData[:-1]], tData[-1]))

    return trainFlowersList


def myEuclidianDist(coordLs1, coordLs2):
    if len(coordLs1) != len(coordLs2):
        print("Error")
        return -1
    su = 0
    for i in range(len(coordLs1)):
        su += pow((coordLs1[i] - coordLs2[i]), 2)
    return sqrt(su)


def testData(trainFlowersList, testFlowersList):
    k = int(input("Input k: "))
    correct = 0
    for i in testFlowersList:
        tmpLs = []
        for ii in trainFlowersList:
            tmpLs.append((myEuclidianDist(i.coord, ii.coord), ii.name))
            tmpLs = sorted(tmpLs, key=lambda pair: pair[0])
        if i.checkAssumption([pair[1] for pair in tmpLs[:k]]):
            correct += 1
    per = 100 * correct/len(testFlowersList)
    print(f"\nAccuracy for given set and k={k} is {per}%")


def guess(trainFlowersList, coord):
    k = int(input("Input k: "))
    tmpLs = []
    for ii in trainFlowersList:
        tmpLs.append((myEuclidianDist(coord, ii.coord), ii.name))
        tmpLs = sorted(tmpLs, key=lambda pair: pair[0])
    tName = statistics.mode([pair[1] for pair in tmpLs[:k]])
    print(f"Assumtion: {tName}")


def main():
    print("Starting")

    trainFlowersList = getFlowerDoneList(getFlowerRowList('../Data/train.txt'))
    testFlowersList = getFlowerDoneList(getFlowerRowList("../Data/test.txt"))
    if "y" == input("Do you want to use test file? y/n "):
        testData(trainFlowersList, testFlowersList)
    else:
        guess(trainFlowersList, [float(c) for c in input("Enter data: ").rstrip().split(',')])


if __name__ == "__main__":
    main()
