from car import Car
from garage import Garage

def project_03():
    infile = open("data.txt", "r")
    outfile = open("garage_report.txt", "w")

    garage_list = read_data(infile)
    garages_and_cars(garage_list, outfile)

    colors = ["white", "yellow", "green", "red", "blue", "black"]
    color_frequency(garage_list, colors, outfile)
    year_frequency(garage_list, outfile)

    newGarage = Garage("Charleston", [])
    move_cars("Chevy", garage_list, newGarage)
    garages_and_cars(garage_list, outfile)

    infile.close()
    outfile.close()


#YOU CODE HERE
def read_data(infile):

    garages_list = []
    for line in infile:
        line = line.split()
        test = line[0]
        location = ""
                                   #or maybe think about making another list of this idk  #the location of this depeneds on how to get the right amount of cars for each garage it needs to be inside outer loop outside inner loop but doesnt work?
        if test[0] == "G":                  #this needs to be a parameter?? to test if the line[0] is garage# ---> I ended up using the letter G to test
            #garagenum = line[0]

            for i in range(1, len(line)):       #this make the name of the location; the rest of the string after garage concatinates to a string which is the location
                location += " " + line[i]
            #print(garagenum,location)
            g = Garage(location,[])
            garages_list.append(g)         #remember this is appending the object address
        else:               #this needs to be the other lines which contain year,make,model, and color
            year = int(line[0])
            make = str(line[1])
            model = str(line[2])
            color = str(line[3])
            #print(year,make,model,color)
            c = Car(year,make,model,color)
            garages_list[len(garages_list)-1].getCars().append(c)  #remember this is appending the object address to the list in an already existing garage.

    return garages_list
def garages_and_cars(garage_list,outfile):
    for garage in garage_list:          #gets the garage out of the list so we can do things with it
        cars = garage.getCars()         #gets the cars[] so we get get the cars out of each garage
        print(f"{garage.getLocation()} garage contains {len(cars)} cars:", file=outfile)  #Los Angeles garage containts 7 cars
        i = 1
        for car in cars:        #gets the car out of the cars[] so we can get or set things to it
            name = car.getMake()        #i dont know why i didn't do this like the others
            print(f"         {i}. {car.getColor()} {car.getYear()} {name} {car.getModel()}",file=outfile)
            i+=1        #this just accumulates so for any size list the cars will just order 1,2,3,4... etc

def color_frequency(garage_list,colors, outfile):
    print("----------------------------------", file=outfile)
    print(f"Across all {len(garage_list)} garages you have:",file=outfile)
    count = len(colors) #gets the length of the colors list LINE 79 CO-PART LINE 71
    # print(count)
    cartotal = 0
    matched = 0
    for colour in colors: #gets the color out of the list of color for every color we run a process to go through all the cars in all garages and pick out the ones that match this color
        num = 0
        for garage in garage_list:#starting the process to go through all cars
            cars = garage.getCars()
            cartotal += len(cars) #takes the list of cars in each garage but this actually repeats too many times because it repeats for every color LINE 79

            for car in cars:
                color = car.getColor()
                if color == colour: #this is where we test the color from the list to the color of the car object
                    num += 1
                    matched+=1
        print(f"         {num} {colour} cars", file=outfile) #printing this for each garage
    other = int((cartotal/count)-matched) #why we divide cartotal by the count of colors
    print(f"         {other} other color cars",file=outfile)
    print(file=outfile)
def year_frequency(garage_list,outfile):
    ten = 0 #these are the accumulators for the amt of cars in each year category
    eleven = 0
    twentyone = 0
    thirtyone = 0
    fortyone = 0
    for garage in garage_list: #pulls the garage obj out of list of garages
        cars = garage.getCars()
        for car in cars: #pulls the car object out of list of cars
            if car.getYear() >= 2012: #these next conditions test the car objects year to see which bucket it falls in.
                ten += 1 #then accumulates a tally for each occurrence
            if car.getYear() < 2012 and car.getYear() >= 2002:
                eleven += 1
            if car.getYear() < 2002 and car.getYear() >= 1992:
                twentyone += 1
            if car.getYear() < 1992 and car.getYear() >= 1982:
                thirtyone += 1
            if car.getYear() < 1982:
                fortyone += 1
    print(f"         {ten} cars 10 years or newer", file=outfile)
    print(f"         {eleven} cars 11-20 years old", file=outfile)
    print(f"         {twentyone} cars 21-30 years old", file=outfile)
    print(f"         {thirtyone} cars 31-40 years old", file=outfile)
    print(f"         {fortyone} cars 41 years or older", file=outfile)
    print("----------------------------------", file=outfile)
def move_cars(make, garage_list, newGarage):
    garage_list.append(newGarage)
    for garage in garage_list:      #opens the list of garages and pulls out a garage to use
        cars = garage.getCars()     #gets the list of cars from the garage (resets every iteration)
        for car in cars:            #gets the car out of the list of cars in the garage (resets every iteration)
            type = car.getMake()    #gets the make of the car object to compare to the parameter (resets every iteration)
            if type == make:    #condition
                garage.removeCar(car)
                newGarage.addCar(car)











if __name__ == "__main__":
    project_03()