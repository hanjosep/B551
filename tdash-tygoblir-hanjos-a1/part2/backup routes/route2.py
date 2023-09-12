#!/usr/local/bin/python3
# using priority Q
# By tdash
# put your routing program here!
import sys
from math import sin, cos, asin, radians, sqrt
from queue import PriorityQueue

global city_gps
global road_seg


def get_distance(start_city, end_city):
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
        return 0
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


# calculate cost
def cost(city, cost_function):
    """
    Function to calculate cost depending on cost_function input
    Args:
        city: city
        cost_function: cost_function
    Returns: a distance depending on cost_function
    """
    if cost_function == "segments":
        return 1
    elif cost_function == "distance":
        return city[1]
    elif cost_function == "time":
        return city[1] / (city[2] + 5)
    elif cost_function == "cycling":
        return city[1] * city[2] * 0.000001


# Return all connecting cities from a city
def successors(city):
    """
    Function to return all connecting cities given a city
    Returns: a parent list of all connecting cities and its data in a list.
    """
    return road_seg.get(city)


def solve(start_city, end_city, cost_function):
    fringe = PriorityQueue()
    fringe.put((0 + get_distance(start_city, end_city), [0, 0, 0, 0, [start_city]]))
    count = 0
    while not fringe.empty():
        count += 1
        current_city = fringe.get()
        # print("popped from Q : ", current_city)
        if current_city[1][4][-1] == end_city:
            return current_city
        con_cities = successors(current_city[1][4][-1])
        # print("con_cities : ", con_cities)
        for city in con_cities:
            # if not city[0].startswith('Jct_'):
            fs = cost(city, cost_function) + get_distance(city[0], end_city)
            route = [current_city[1][0] + 1, current_city[1][1] + city[1],
                     current_city[1][2] + city[1] / city[2],
                     current_city[1][3] + city[1] * city[2] * 0.000001, current_city[1][4] + [city[0]]]
            fringe.put((fs, route))

        # if count > 40:
        #     sys.exit()

    return False


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
