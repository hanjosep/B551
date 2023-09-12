import sys
from math import sin, cos, asin, radians, sqrt
from queue import PriorityQueue

global road_seg, city_gps


def create_gps_dict():
    """
    Function to read a text file and create a dictionary of cities as key and their longitude and latitude as values.
    Returns: a dictionary
    """
    gps = {}
    with open("city-gps.txt") as f:
        for line in f:
            (city, latitude, longitude) = line.split()
            gps[city] = [float(latitude), float(longitude)]
        return gps


def create_road_seg_dict():
    """
    Function to read a text file and create a dictionary of road segments.
    Returns: a dictionary
    """
    road_seg = {}
    with open("road-segments.txt") as f:
        for line in f:
            (start_city, end_city, length, speed_limit, highway_name) = line.split()
            if start_city not in road_seg:
                road_seg[start_city] = [[end_city, int(length), int(speed_limit), highway_name]]
            else:
                road_seg[start_city].append([end_city, int(length), int(speed_limit), highway_name])
            if end_city not in road_seg:
                road_seg[end_city] = [[start_city, int(length), int(speed_limit), highway_name]]
            else:
                road_seg[end_city].append([start_city, int(length), int(speed_limit), highway_name])

        return road_seg


# begin building the road dictionaries and connections.
city_gps = create_gps_dict()
road_seg = create_road_seg_dict()


def get_distance(start_city, end_city, city_gps):
    """
    Function to calculate euclidean distance between cities
    Args:
        start_city: start_city
        end_city: end_city
        city_gps: city GPS dictionary
    Returns: a float distance
    """
    if start_city == end_city:
        return 0
    # if a city is missing a gps coordinate return distance 0
    if start_city not in city_gps or end_city not in city_gps:
        return float(0)
    else:
        [st_lat, st_long] = city_gps.get(start_city)
        [end_lat, end_long] = city_gps.get(end_city)
        # courtesy - https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance
        # -between-two-gps-points convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [st_long, st_lat, end_long, end_lat])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6372800
        return c * r * 0.000621371


# heuristic from the popped city to the end city.
def state_heuristic(city, end_city, cost_function):
    # print(city)
    cityname = city[0]
    mph = city[2]
    distance = float(get_distance(cityname, end_city, city_gps))
    if distance == 0:
        return 0
    if cost_function == "segments":
        return 0
    if cost_function == "distance":
        return distance
    if cost_function == 'time':
        time = float(float(distance) / (mph + 5))
        return time
    if cost_function == 'cycling':
        return distance * mph * 0.000001


def successors(city):
    """
    Function to return all connecting cities given a city
    Returns: a parent list of all connecting cities and its data in a list.
    """
    return road_seg.get(city)


def solve(start_city, end_city, cost_function):
    fringe = PriorityQueue()
    fringe.put((0, [0, 0, 0, 0, [start_city]]))

    while not fringe.empty():
        got = fringe.get()
        current_h_and_c = got[0]
        result = got[1]
        segments_so_far = got[1][0]
        distance_so_far = got[1][1]
        time_so_far = got[1][2]
        cycling_so_far = got[1][3]
        route_so_far = got[1][4]

        current_city = got[1][4][-1]
        # print(current_city)
        if current_city == end_city:
            return result
        con_cities = successors(current_city)
        # print("con_cities : ",con_cities)
        for city in con_cities:
            new_heuristic = float(state_heuristic(city, end_city, cost_function))
            c = len(got[1][4]) - 1
            while cost_function != "segments" and new_heuristic == 0:
                prev_town = got[1][4][c]
                newcity = [prev_town, city[1], city[2], city[3]]
                new_heuristic = state_heuristic(newcity, end_city, cost_function)
                c -= 1
            newroute = route_so_far + [city[0]]
            segment_to_add = 1 + segments_so_far
            distance_to_add = city[1] + distance_so_far
            time_to_add = float(float(city[1]) / (city[2] + 5)) + float(time_so_far)
            cycling_to_add = city[1] * city[2] * 0.000001 + cycling_so_far
            if cost_function == 'segments':
                fringe.put((segment_to_add + new_heuristic,
                            [segment_to_add, distance_to_add, time_to_add, cycling_to_add, newroute]))
            if cost_function == 'distance':
                fringe.put((distance_to_add + new_heuristic,
                            [segment_to_add, distance_to_add, time_to_add, cycling_to_add, newroute]))
            if cost_function == 'time':
                fringe.put((time_to_add + new_heuristic,
                            [segment_to_add, distance_to_add, time_to_add, cycling_to_add, newroute]))
            if cost_function == 'cycling':
                fringe.put((cycling_to_add + new_heuristic,
                            [segment_to_add, distance_to_add, time_to_add, cycling_to_add, newroute]))


# The main function
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise (Exception("Error: Please enter agrs in format [start-city] [end-city] [cost-function]"))

    start_city = sys.argv[1]
    end_city = sys.argv[2]
    cost_function = sys.argv[3]

    if cost_function not in ["segments", "distance", "time", "cycling"]:
        raise (Exception("Wrong cost_function choice.Choose one from segments or distance or time or cycling"))

    if start_city == end_city:
        raise (Exception("start_city and end_city cannot be same"))

    city_gps = create_gps_dict()
    # print(city_gps)

    road_seg = create_road_seg_dict()
    # print(road_seg)

    # distance = get_distance(start_city, end_city, city_gps)
    # print("Euclidean distance : ",distance)

    # connecting_cities = successors(city, city_visited, road_seg)
    # print(connecting_cities)

    # # cost = cost(city, cost_function)
    # # print(cost)

    result = solve(start_city, end_city, cost_function)
    print(result)