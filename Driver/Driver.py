import random

from Map.CountryMap import City
from main import calculateDistance


class Driver:
    listOfCities = []
    distArray = []

    def __init__(self, name, listOfCities):
        self.name = name
        self.listOfCities = listOfCities

    def calculateRouteDistance(self):
        distance = 0
        for x in range (len(self.listOfCities)-1):
            cityOrigin = self.listOfCities[x]
            cityDestination = self.listOfCities[x+1]
            twoPointDist = calculateDistance(cityOrigin.xPos, cityOrigin.yPos, cityDestination.xPos, cityDestination.yPos)
            distance += twoPointDist
        return distance

    def listDriverCities(self):
        print("Listing cities")
        for x in range(len(self.listOfCities)):
            print(self.name + ", City." + str(x) + ": " + str(self.listOfCities[x].xPos) + " " + str(self.listOfCities[x].yPos))

    # swaps order of two consecutive cities based on randomly generated number
    def changeOrderOfTwoConsecutiveCities(self):
        listLength = len(self.listOfCities)
        swapIndex1 = 1
        if listLength > 4:
            swapIndex1 = random.randint(1, listLength-3)        # first and last city must be Base City
        elif listLength == 4:
            swapIndex1 = 1  # first and last city must be Base City
        else:
            return
        swapIndex2 = swapIndex1+1
        self.listOfCities[swapIndex1], self.listOfCities[swapIndex2] = self.listOfCities[swapIndex2], self.listOfCities[swapIndex1]


    def changeOrderOfTwoRandomCities(self):
        listLength = len(self.listOfCities)
        swapIndex1 = random.randint(1, listLength-2)        # first and last city must be Base City
        swapIndex2 = random.randint(1, listLength-2)
        # case when its BASE CITY xNumbOfCities BASE
        if listLength > 3:
            while swapIndex1 == swapIndex2:
                swapIndex2 = random.randint(1, listLength-2)
        self.listOfCities[swapIndex1], self.listOfCities[swapIndex2] = self.listOfCities[swapIndex2], self.listOfCities[swapIndex1]

    def changeIndex(self):
        listLength = len(self.listOfCities)
        if listLength <= 4:
            return
        index1 = random.randint(1, len(self.listOfCities)-2)
        index2 = random.randint(1, len(self.listOfCities)-3)

        # if listLength > 3:
        #     while index1 == index2:
        #         index2 = random.randint(1, listLength-2)
        self.listOfCities.insert(index2, self.listOfCities.pop(index1))
