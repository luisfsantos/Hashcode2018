from solution.roads import Ride, Car

def pick_ride(car, rides, bonus):
    best_ride = (None, 0)
    for ride in rides:
        if ride.lf <= car.arrival_time_of_ride(ride):
            continue # go to next ride
        else:
            if car.arrival_time_of_ride(ride) >= ride.es:
                score = ride.distance
            else:
                score = bonus + ride.distance - abs(ride.es - car.arrival_time_of_ride(ride))
            # calculate score and check if it is larger than best_ride, substitute if True
        if best_ride:
            best_ride = best_ride if score <= best_ride[1] else (ride, score)
        else:
            best_ride = (ride, score)
        #TODO- cutoff the loop when gains are not going up (es is always gonna be achieved but waiting time is going up)

    return best_ride[0]
