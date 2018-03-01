import argparse
from solution.parse import read_input
from algorithms.optimal_ride_v0 import pick_ride
from solution.roads import Car

parser = argparse.ArgumentParser(
    description="This is a file read for google hashcode 2018"
)
parser.add_argument("-f", action='store',
                    dest='file_path',
                    help='File path of the cache reading challenge.')
parser.add_argument("-p", action='store',
                    dest='prob',
                    default=1.0,
                    help='Propability of a request being taken into consideration')

results = parser.parse_args()

#Input read with a list of all the rides
global_vars, rides = read_input(results.file_path)

# Init cars
num_cars = global_vars['F']
cars = [Car() for _ in range(num_cars)]

final_cars = cars.copy() # .copy() is faster than slicing
#For each car pick a ride
turn_available = True
while (turn_available):
    #TODO - order rides by earliest start
    for car in cars[:]:
        if car.turn_when_available >= global_vars["T"]:
            cars.remove(car)
        ride = pick_ride(car, rides, global_vars["B"])
        if ride is None:
            # remove car from cars list, since it won't work
            cars.remove(car)
        else:
            car.add_ride(ride)
            rides.remove(ride)

    if len(cars) == 0:
        turn_available = False



for car in final_cars:
    print(f'{len(car.rides)} {car.get_str_ids()}')
