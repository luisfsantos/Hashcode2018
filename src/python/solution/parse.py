from solution.roads import Intersection, Ride


def read_input(filepath):
    input_read = {}
    with open(filepath, 'r') as file:
        curr_line = file.readline()
        line_dict = curr_line.split()
        input_read["R"] = int(line_dict[0]) #number of rows of the grid (1 ≤ R ≤ 10000)
        input_read["C"] = int(line_dict[1]) #number of columns of the grid (1 ≤ C ≤ 10000)
        input_read["F"] = int(line_dict[2]) #number of vehicles in the fleet (1 ≤ F ≤ 1000)
        input_read["N"] = int(line_dict[3]) #number of rides (1 ≤ N ≤ 10000)
        input_read["B"] = int(line_dict[4]) #per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
        input_read["T"] = int(line_dict[5]) #number of steps in the simulation (1 ≤ T ≤ 10^9)
        rides = []
        for curr_line in file:
            line_dict = curr_line.split()
            start = Intersection(int(line_dict[0]), int(line_dict[1]))
            end = Intersection(int(line_dict[2]), int(line_dict[3]))
            ride = Ride(start, end, int(line_dict[4]), int(line_dict[5]))
            rides.append(ride)

    return input_read, rides
