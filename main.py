import copy
import random

from Map.CountryMap import *
from Driver.Driver import *
import matplotlib.pyplot as plt

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # input variables
    numberOfDrivers = 8 # notUsed
    temperature = 20
    finalTemperature = 0.1
    temperatureDivider = 0.95
    numberOfTries = 200
    maxNumberOfTries = 10000000
    currentNumberOfTries = 0
    firstSolution = 99999999999
    baseCity = City("Base", 0, 0)


    # board creation
    countryMap = CountryMap("Map", temperature)
    countryMap.createMap()

    # main algorithm
    """
    generatedNumber = random.randint(2, len(countryMap.listOfCities)-2)
    print("Number: " + str(generatedNumber))
    numberOfCitiesFirstDriver = generatedNumber
    numberOfCitiesSecondDriver = len(countryMap.listOfCities) - numberOfCitiesFirstDriver
"""
    # more than two drivers
    listNumberOfCitiesForEachDriver = []                            # lista ile miast moze miec kazdy kierowca
    remainingNumberOfCities = len(countryMap.listOfCities)          # pozostala ilosc miast
    generatedNumber = random.randint(2, len(countryMap.listOfCities)-((numberOfDrivers-1)*2))       # pierwszy kierowca moze miec: ilosc_miast - 3kierowcy po 2 miasta
    listNumberOfCitiesForEachDriver.append(generatedNumber)                                         # dodaje ilosc miast dla pierwszego kierowcy do listy
    remainingNumberOfCities = len(countryMap.listOfCities) - generatedNumber                        # pozostala ilosc miast = dlugosc mapy - ilosc dla pierwszego kierowcy

    for x in range(numberOfDrivers-2):                                                              # dla kazdego kierowcy oprocz pierwszego
        #remainingNumberOfCities = len(countryMap.listOfCities) - generatedNumber
        value = remainingNumberOfCities - ((numberOfDrivers - x - 2)*2)
        print(value)
        if value == 2:
            generatedNumber = 2
        else:
            generatedNumber = random.randint(2, value)
        listNumberOfCitiesForEachDriver.append(generatedNumber)
        remainingNumberOfCities = remainingNumberOfCities - generatedNumber

    listNumberOfCitiesForEachDriver.append(remainingNumberOfCities)


    # initial solution - order from file
    driversList = []


    #firstDriverCityOrder = []
    #secondDriverCityOrder = []
    bestSolutionDriversList = []
    # add to all drivers first city in pos 0 and int the last pos - they need to start from base and end in base

    citiesShift = 0
    for x in range(numberOfDrivers):                                    # for each driver
        driverCityOrder = []
        driverCityOrder.append(baseCity)
        for y in range(listNumberOfCitiesForEachDriver[x]):             # number of cities for each driver
            driverCityOrder.append(countryMap.listOfCities[y+citiesShift])
        driverCityOrder.append(baseCity)
        citiesShift = citiesShift + listNumberOfCitiesForEachDriver[x]
        driver = Driver("driver" + str(x), driverCityOrder)
        driversList.append(driver)





    """
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
    """
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
            newSolutionChoice = random.randint(1, 4)
            print("NUMB: " + str(newSolutionChoice))
            # copying list of drivers
            driversListCopy = copy.deepcopy(driversList)
            # Swapping order of two consecutive cities for one random driver
            if newSolutionChoice == 1:
                print("Creating new solution - option 1 was chosen.")
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                driversListCopy[randomDriverIndex].changeOrderOfTwoConsecutiveCities()
            # swapping order of two, not necessary consecutive cities for one random driver
            if newSolutionChoice == 2:
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                driversListCopy[randomDriverIndex].changeOrderOfTwoRandomCities()
            if newSolutionChoice == 3:
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                driversListCopy[randomDriverIndex].changeIndex()
            # removing one city from one driver and adding it to another drivers list
            if newSolutionChoice == 4:
                randomDriverIndex = random.randint(0, numberOfDrivers-1)
                randomDriverIndex2 = random.randint(0, numberOfDrivers-1)
                # check index2
                if len(driversListCopy[randomDriverIndex].listOfCities) >= 5:
                    if numberOfDrivers > 2:
                        while(randomDriverIndex2 == randomDriverIndex):
                            randomDriverIndex2 = random.randint(0, numberOfDrivers - 1)
                    elif numberOfDrivers == 2:
                        randomDriverIndex2 = numberOfDrivers - (randomDriverIndex+1)
                    randomCityIndexRemove = random.randint(1, len(driversListCopy[randomDriverIndex].listOfCities)-2)
                    randomCityIndexAdd = random.randint(1, len(driversListCopy[randomDriverIndex2].listOfCities)-1)
                    # adding city to a list
                    driversListCopy[randomDriverIndex2].listOfCities.\
                        insert(randomCityIndexAdd, driversListCopy[randomDriverIndex].listOfCities[randomCityIndexRemove])
                    # removing city from a list
                    driversListCopy[randomDriverIndex].listOfCities.pop(randomCityIndexRemove)
            print("Temperature: " + str(temperature))
            newSolution = 0
            for z in range(len(driversListCopy)):
                newSolution = newSolution + driversListCopy[z].calculateRouteDistance()
            print("Before deciding: " + str(newSolution))
            result = math.exp((currentSolution - newSolution) / temperature)
            randomNumber = random.random()
            if newSolution < bestFoundSolution:
                bestFoundSolution = newSolution
                for w in range(numberOfDrivers):
                    bestSolutionDriversList.append(driversListCopy[w])
            if randomNumber < result or newSolution < currentSolution:
            #if newSolution < currentSolution:
                currentSolution = newSolution
                newSolution = 0
                driversList = driversListCopy
                print("ACCEPTED")

            print("After try " + str(currentSolution))
        temperature = temperature * temperatureDivider

    print("First solution: " + str(firstSolution))
    print("Final solution: " + str(currentSolution))
    print("Best solution: " + str(bestFoundSolution))

    def createDataToPlot():

        global listOfListsX
        global listOfListsY

        pointx = []
        pointy = []
        for x in range((len(driversList))):
            for y in range(len(driversList[x].listOfCities)):

                pointx.append(driversList[x].listOfCities[y].xPos)
                pointy.append(driversList[x].listOfCities[y].yPos)

        listTempX = []
        listTempY = []
        listOfListsX= []
        listOfListsY = []


        for i in range(len(pointx)):

            if pointx[i] == 0 and pointx[i-1]:
                listTempX.append(pointx[i])
                listOfListsX.append(listTempX)
                listTempX = []
                listTempY.append(pointy[i])
                listOfListsY.append(listTempY)
                listTempY = []
            else:
                listTempX.append(pointx[i])
                listTempY.append(pointy[i])

        #print("x",pointx)
        #print("y",pointy)
        #print(listOfListsX)
        #print(listOfListsY)


        return listOfListsX,listOfListsY

    # printing final order of cities.
    for x in range(numberOfDrivers):
        driversList[x].listDriverCities()


    createDataToPlot()



    def drawResult(listOfListX,listOfListsY):

        color = ['red', 'blue', 'black', 'green', 'yellow', "orange", "purple", "pink"]
        actual_color = []
        pointx = listOfListX
        pointy = listOfListsY

        for i in range(len(pointx)):
            for j in range(len(pointx[i])):
                plt.scatter(pointx[i][j], pointy[i][j], s=10, color=color[i])

        for y in range(len(pointx)):
            actual_color.append(color[y])
            plt.plot(pointx[y], pointy[y], color=actual_color[y])
        plt.show()

    drawResult(listOfListsX,listOfListsY)

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
    dist = math.sqrt(math.pow((city1X - city2X), 2) + math.pow((city1Y - city2Y), 2))
    return dist

# todo test temperatures for larger amount of cities
# todo for creating graphs use <driversList>
# todo and plot a path for each driver in driversList

def copyDriverList(list):

    return