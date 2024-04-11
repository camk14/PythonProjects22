from car import Car

class Garage:
   # YOUR CODE HERE
    def __init__(self, location, cars):
        self.location = str(location)
        self.cars = cars

    def getLocation(self): return self.location
    def getCars(self): return self.cars
    def addCar(self,Car): self.cars.append(Car)
    def removeCar(self,car): self.cars.remove(car)





def main():
    cars = [Car(2022, "Audi", "Q3", "charcoal"), Car(2022, "Ford", "Bronco", "green")]
    garage = Garage("New York", cars)
    if garage.getLocation() == "New York": print("getLocation works correctly: PASS")
    else: print("something is wrong with getLocation or your constructor")
    if garage.getCars() == cars: print("getCars works correctly: PASS")
    else: print("something is wrong with getCars or your constructor or the Car constructor")

    car = Car(2019, "Volvo", "CX90", "white")
    garage.addCar(car)
    if garage.getCars()[2] == car: print("addCar works correctly: PASS")
    else: print("something is wrong with addCar: FAIL")
    garage.removeCar(car)
    if car not in garage.getCars(): print("removeCar works correctly: PASS")
    else: print("something is wrong with removeCar: FAIL")


if __name__ == "__main__":
    main()