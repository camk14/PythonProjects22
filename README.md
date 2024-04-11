# Project Overview

The point of this project was to utilize concepts in Python 3.10 that were taught in my Python summer class. 

## Key Concepts

- loops
- nested loops
- multi-way decisions
- functions
- formatted output
- file i/o
- objects and classes
-arrays

## Problem Statement

You love cars, and you have cars in several garages. Write a program for garage and car accounting where data comes from an input file and a report is written to an output file.

## File Explanation

### `project_03.py`

This is the main script where the core logic of the program is implemented.

##Overview
* 		Imports and Initial Setup: The script imports Car and Garage classes from separate modules (car.py and garage.py). It defines a project_03 function which is the main entry point of the script.
* 		File Handling: It opens two files - data.txt for reading data and garage_report.txt for writing reports. The data file is expected to contain information about garages and cars, formatted in a specific way.
* 		Data Reading and Object Creation: The read_data function reads each line from the data.txt file. Lines that start with "G" are considered garage information, and subsequent lines are assumed to be car information until the next garage entry is found. For each garage, a Garage object is created with an empty list of cars. For each car, a Car object is created and added to the most recently created garage's list of cars. The function returns a list of garage objects, each containing its respective cars.
* 		Reporting: Several reporting functions are defined and called in sequence:
    * garages_and_cars lists all garages and the cars they contain in the garage_report.txt.
    * color_frequency reports the frequency of cars by color across all garages.
    * year_frequency reports the distribution of cars by age categories.
* 		Moving Cars: The move_cars function moves all cars of a given make (in this case, "Chevy") to a new garage created within the function (located in "Charleston"). This new garage is also added to the list of garages.
* 		File Closure: Finally, the input and output files are closed.

##Key Functions:
* read_data(infile): Reads garage and car data from the input file, creating Garage and Car objects accordingly, and organizes them into a list.
* garages_and_cars(garage_list, outfile): Writes information about each garage and its cars to the output file.
* color_frequency(garage_list, colors, outfile): Analyzes and reports the frequency of cars by color across all garages.
* year_frequency(garage_list, outfile): Reports the number of cars in various age categories across all garages.
* move_cars(make, garage_list, newGarage): Moves all cars of a specified make to a newly created garage.

### `car.py`

This module contains the definitions related to cars, such as classes and functions for managing car attributes.

In this module the car class is defined

It includes basic class definition, object instantiation, attribute initialization, and method usage

### `garage.py`

This module is responsible for managing garage-related functionalities, including storing and managing multiple cars.

In this module the garage class is defined.  

It includes methods for initializing the garage with a location and a list of cars, adding a new car to the garage, removing a car from the garage, and getting the garage's location and the list of cars stored in it.

