# Generation of cities
from Map.City import City
from random import randint
import numpy as np
import math


class CountryMap:
    listOfCities = []
    distArray = []

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def createMap(self):
        with open('Data/data6.txt') as f:
        #with open('Data/data15.txt') as f:
        #with open('Data/example8.txt') as f:
        #with open('Data/data51.txt') as f:
            lines = f.readlines()
        # numberOfCities is a value hardcoded in a text file
        numberOfCities = int(lines[0])
        # adds the cities and lists them
        for x in range(numberOfCities):
            pos = lines[int(x)+1].split()
            cityName = "city_" + str(int(x) + 1)
            city = City(cityName, int(pos[0]), int(pos[1]))       #todo
            CountryMap.listOfCities.append(city)
            CountryMap.listOfCities[int(x)].listCity()

    def calculateDistance(self, city1X, city1Y, city2X, city2Y):
        #print("City 1 xPos in funct: " + str(city1X))
        if city1X != city2X and city1Y != city2Y:
            dist = math.sqrt(math.pow((city1X - city2X), 2) + math.pow((city1Y - city2Y), 2))
            #print("DIST in funct: " + str(dist))
            return dist
        else:
            return 0



    """
    losowanie ilosci miast dla kierowcow z randoma rozkladu normalnego ( minimum i max dla 1 kierowcy)
    
    ustalenie pobliskiego rozwiazania - zamiana kolejnosci dwoch miast (1. dwoch sasiednich czy 2. dwoch dowolnych?)
    3. (inna opcja - biore częsc rozwiazania, czyli na przyklad 3 kolejne miasta i obracam ich kolejnosc - ostatni na pierwsze itd)
    opcja - ustawic prawd ktore z tych rozwiazan bedzie wybrane?
    4. (inna opcja - wziecie jednego miasta dla kierowcy A w losowym miejscu i danie go kierowcy B w losowym miejscu) - trzeba jeszcze
    wylosowac komu zabieramy miasto z listy
    pierwsza i czwarta opcja musi być
    
    kroki:
    - podzielenie sie miastami ( X miast 1 kierowca, reszta drugi)
    - rozwiazanie poczatkowe - wziac kolejnosc z pliku
    - algorytm - obliczyc wartosc funkcji celu, wylosowac nowe rozwiazanie, obliczyc wart funkcji celu i prawdopodobienstwo z 0,1 
    czy zamieniac
    
    zmienianie temperatury co ileś tam prób czy iteracji zamiany miast
    """