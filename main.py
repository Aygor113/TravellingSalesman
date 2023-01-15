import random

from Map.CountryMap import *
from Driver.Driver import *

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # input variables
    numberOfDrivers = 2 # notUsed
    temperature = 40
    finalTemperature = 20
    temperatureDivider = 0.8
    numberOfTries = 5
    maxNumberOfTries = 40
    currentNumberOfTries = 0
    firstSolution = 99999999999

    # board creation
    countryMap = CountryMap("Map", temperature)
    countryMap.createMap()
    #countryMap.createDistanceArray()

    # main algorithm
    generatedNumber = random.randint(2, len(countryMap.listOfCities)-2)
    print("Number: " + str(generatedNumber))
    numberOfCitiesFirstDriver = generatedNumber
    numberOfCitiesSecondDriver = len(countryMap.listOfCities) - numberOfCitiesFirstDriver

    # initial solution - order from file
    driversList = []
    firstDriverCityOrder = []
    secondDriverCityOrder = []
    bestSolutionDriversList = []
    # add to all drivers first city in pos 0 and int the last pos - they need to start from base and end in base
    baseCity = City("Base", 0, 0)

    # driver 1
    firstDriverCityOrder.append(baseCity)
    for x in range (numberOfCitiesFirstDriver):
        firstDriverCityOrder.append(countryMap.listOfCities[x])
    firstDriverCityOrder.append(baseCity)

    # driver2
    secondDriverCityOrder.append(baseCity)
    for y in range (numberOfCitiesSecondDriver):
        secondDriverCityOrder.append(countryMap.listOfCities[len(countryMap.listOfCities) - numberOfCitiesSecondDriver + y])
    secondDriverCityOrder.append(baseCity)

    # Creation of the drivers - salesmen
    driver1 = Driver("driver1", firstDriverCityOrder)
    driver2 = Driver("driver2", secondDriverCityOrder)

    driversList.append(driver1)
    driversList.append(driver2)

    driver1.listDriverCities()
    driver2.listDriverCities()

    # solution is a sum of distances covered by all drivers
    newSolution = 0
    currentSolution = 0
    bestFoundSolution = 99999999
    for z in range(len(driversList)):
        currentSolution = currentSolution + driversList[z].calculateRouteDistance()
    firstSolution = currentSolution
    while temperature >= finalTemperature and currentNumberOfTries <= maxNumberOfTries:
        for x in range(numberOfTries):
            currentNumberOfTries = currentNumberOfTries+1
            print("Current number of tries: " + str(currentNumberOfTries))
            # todo tutaj losowe rozwiązanie
            newSolutionChoice = random.randint(1, 3)
            print("NUMB: " + str(newSolutionChoice))
            # Swapping order of two consecutive cities for one random driver
            if newSolutionChoice == 1:
                print("Creating new solution - option 1 was chosen.")
                # todo check if base is included here
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                driversList[randomDriverIndex].changeOrderOfTwoConsecutiveCities()
            # swapping order of two, not necessary consecutive cities for one random driver
            if newSolutionChoice == 2:
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                driversList[randomDriverIndex].changeOrderOfTwoRandomCities()
            # removing one city from one driver and adding it to another drivers list
            if newSolutionChoice == 3:
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                randomDriverIndex2 = random.randint(0, numberOfDrivers-1)
                # check index2
                if len(driversList[randomDriverIndex].listOfCities) >= 4:
                    if numberOfDrivers > 2:
                        while(randomDriverIndex2 == randomDriverIndex):
                            randomDriverIndex2 = random.randint(0, numberOfDrivers - 1)
                    elif numberOfDrivers == 2:
                        randomDriverIndex2 = numberOfDrivers - (randomDriverIndex+1)
                    #if len(driversList[randomDriverIndex].listOfCities)-2 == 1:
                    #    randomCityIndexRemove = 1
                    randomCityIndexRemove = random.randint(1, len(driversList[randomDriverIndex].listOfCities)-2)
                    #if len(driversList[randomDriverIndex2].listOfCities)-2 == 1:
                    #    randomCityIndexAdd = 1
                    #else:
                    randomCityIndexAdd = random.randint(1, len(driversList[randomDriverIndex2].listOfCities)-1)
                    # adding city to a list
                    driversList[randomDriverIndex2].listOfCities.\
                        insert(randomCityIndexAdd, driversList[randomDriverIndex].listOfCities[randomCityIndexRemove])
                    # removing city from a list
                    driversList[randomDriverIndex].listOfCities.pop(randomCityIndexRemove)
            newSolution = 0
            for z in range(len(driversList)):
                newSolution = newSolution + driversList[z].calculateRouteDistance()
            print("New solution to be or not be accepted: " + str(newSolution))
            result = math.exp((currentSolution - newSolution) / temperature)
            randomNumber = random.random()
            if newSolution < bestFoundSolution:
                bestFoundSolution = newSolution
                for w in range(numberOfDrivers):
                    bestSolutionDriversList.append(driversList[w])
            if randomNumber < result or newSolution < currentSolution:
                currentSolution = newSolution
                newSolution = 0

            print("Current solution after choice to be or not be accepted: " + str(currentSolution))

    print("First solution: " + str(firstSolution))
    print("Final solution: " + str(currentSolution))
    print("Best solution: " + str(bestFoundSolution))


def createDistanceArray(self, countryMap):
    numberOfCities = len(countryMap.listOfCities)
    distArray = np.empty(shape=(numberOfCities, numberOfCities))
    for i in range(numberOfCities):
        for j in range(numberOfCities):
            print("City 1 xPos: " + str(countryMap.listOfCities[i].xPos))
            dist = countryMap.calculateDistance(self, countryMap.listOfCities[i].xPos,
                                                countryMap.listOfCities[i].yPos,
                                                countryMap.listOfCities[j].xPos, countryMap.listOfCities[
                                                    j].yPos)  # todo work on city object instead of coordinates
            distArray[i][j] = dist
            print("DISTANCE: " + str(dist))
    return distArray


def calculateDistance(city1X, city1Y, city2X, city2Y):
    if city1X != city2X and city1Y != city2Y:
        dist = math.sqrt(math.pow((city1X - city2X), 2) + math.pow((city1Y - city2Y), 2))
        return dist
    else:
        return 0

# todo test temperatures for larger amount of cities
# todo for creating graphs use <driversList>
# todo and plot a path for each driver in driversList