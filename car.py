class Car:
    # YOUR CODE HERE
    def __init__(self, year, make, model,color):
        self.year = int(year)
        self.make = str(make)
        self.model = str(model)
        self.color = str(color)

    def getYear(self):
        return self.year
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color


def main():
    car = Car(2022, "Audi", "Q3", "charcoal")
    if car.getMake() == "Audi": print("getMake works correctly: PASS")
    else: print("something is wrong with getMake or your constructor: FAIL")
    if car.getModel() == "Q3": print("getModel works correctly: PASS")
    else: print("something is wrong with getModel or your constructor: FAIL")
    if car.getYear() == 2022: print("getYear works correctly: PASS")
    else: print("something is wrong with getYear or your constructor: FAIL")
    if car.getColor() == "charcoal": print("getColor works correctly: PASS")
    else: print("something is wrong with getColor or your constructor: FAIL")

if __name__ == "__main__":
    main()