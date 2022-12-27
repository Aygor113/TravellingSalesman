# Generation of cities
from map.City import City
from random import seed
from random import randint
import numpy as np
import math


class CountryMap:
    listOfCities = []

    def __init__(self, name):
        self.name = name

    """
    def generateCties(self, dimension):
        seed(1)
        for x in range(self.numberOfCities):
            xPos = randint(0, dimension)
            yPos = randint(0, dimension)
            while (CountryMap.ValidateCityPosition(xPos, yPos) == "false"):
                xPos = randint(0, dimension)
                yPos = randint(0, dimension)
            if (CountryMap.ValidateCityPosition(xPos, yPos) == "true"):
                city = City("city_" + str(x + 1), xPos, yPos)
                CountryMap.listOfCities.append(city)
    """

    def createMap(self):
        with open('Data/makuch.txt.txt') as f:
            lines = f.readlines()
        # numberOfCities is a value hardcoded in a text file
        numberOfCities = int(lines[0])
        # adds the cities and lists them
        for x in range(numberOfCities):
            pos = lines[int(x)+1].split()
            cityName = "city_" + str(int(x) + 1)
            city = City(cityName, int(pos[0]), int(pos[1]))
            CountryMap.listOfCities.append(city)
            CountryMap.listOfCities[int(x)].listCity()

    def createDistanceArray(self):
        numberOfCities = len(CountryMap.listOfCities)
        distArray = np.empty(shape=(numberOfCities,numberOfCities))
        for i in range(numberOfCities):
            for j in range (numberOfCities):
                print("City 1 xPos: " + str(CountryMap.listOfCities[i].xPos))
                dist = CountryMap.calculateDistance(self, CountryMap.listOfCities[i].xPos, CountryMap.listOfCities[i].yPos,
                                                    CountryMap.listOfCities[j].xPos, CountryMap.listOfCities[j].yPos ) # todo correct error
                distArray[i][j] = dist
                print("DISTANCE: " + str(dist))


    def calculateDistance(self, city1X, city1Y, city2X, city2Y):
        print("City 1 xPos in funct: " + str(city1X))
        if city1X != city2X and city1Y != city2Y:
            dist = math.sqrt(math.pow((city1X - city2X), 2) + math.pow((city1Y - city2Y), 2))
            print("DIST in funct: " + str(dist))
            return dist
        else:
            return 0

