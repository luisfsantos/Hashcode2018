class Intersection(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_steps(i1, i2):
    return abs(i1.x - i2.x) + abs(i1.y - i2.y)

class Ride(object):
    counter = 0
    def __init__(self, start, end, es, lf):
        self.id = Ride.counter
        self.start = start
        self.end = end
        self.es = es
        self.lf = lf
        self.distance = distance_steps(self.start, self.end)
        Ride.counter += 1

    def distance_from_intersection_to_start(self, interseciton):
        return distance_steps(self.start, interseciton)

    def distance_from_intersection_to_end(self, intersection):
        return distance_steps(self.end, intersection)


class Car(object):
    def __init__(self):
        self.rides = []
        self.available_position = Intersection(0, 0)
        self.turn_when_available = 0

    def arrival_time_of_ride(self, ride):
        distance_to_ride_start = ride.distance_from_intersection_to_start(self.available_position)
        return max(distance_to_ride_start, ride.es) + ride.distance

    def add_ride(self, ride):
        self.rides += [ride]
        distance_to_ride_start = ride.distance_from_intersection_to_start(self.available_position)
        self.turn_when_available = max(distance_to_ride_start, ride.es) + ride.distance
        self.available_position = ride.end

    def _get_ride_str_id(self, ride):
        return str(ride.id)

    def get_str_ids(self):
        return ' '.join(map(self._get_ride_str_id, self.rides))
