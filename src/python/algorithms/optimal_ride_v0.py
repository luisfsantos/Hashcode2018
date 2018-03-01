from solution.roads import Ride, Car

def pick_ride(car, rides, bonus, T):
    best_ride = (None, 0)
    for ride in rides:
        if ride.lf <= car.arrival_time_of_ride(ride)+ ride.distance + 1:
            continue # go to next ride
        else:
            if car.arrival_time_of_ride(ride) >= ride.es:
                score = ride.distance
            else:
                score = bonus + ride.distance
            # calculate score and check if it is larger than best_ride, substitute if True
        best_ride = best_ride if score <= best_ride[1] else (ride, score)
        #TODO- cutoff the loop when gains are not going up (es is always gonna be achieved but waiting time is going up)

    return best_ride[0]
