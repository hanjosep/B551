#!/usr/local/bin/python3

# By tdash
# put your routing program here!
import sys
from math import sin, cos, asin, radians, sqrt
# notes from Josep:
# TODO: set global variables. city_gps and road_seg never change when we go through this code.
# Clarifications:
#   cost/heuristic function estimates how far the state is from the goal state. Not to be conflated with the path traversed already. 
#   solve function: currently in BFS mode. Convert to A*. 
# from queue import PriorityQueue
# customers = PriorityQueue()
# customers.put((2, "Harry"))
# customers.put((3, "Charles"))
# customers.put((1, "Riya"))
# customers.put((4, "Stacy"))
# while not customers.empty() 
#     popped  = customers.get
#     print(popped)
#     # print(customers.get())
# 
# Priority value will depend on the user input, where the easiest is the number of segments.

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
        return 0
    elif cost_function == "distance":
        return city[1]
    elif cost_function == "time":
        return city[1] / (city[2] + 5)
    elif cost_function == "cycling":
        return city[1] * city[2] * 0.000001


# Return all connecting cities from a city
def successors(city, city_visited):
    """
    Function to return all connecting cities given a city
    Returns: a parent list of all connecting cities and its data in a list.
    """
    connected_cities = []
    for city in road_seg.get(city):
        if city[0] not in city_visited:
            connected_cities.append(city)

    return connected_cities


def solve(start_city, end_city, cost_function):
    city_visited = [start_city]
    result = [0, 0, 0, 0]
    fringe = [start_city]
    while len(fringe) > 0:
        current_city = fringe.pop()
        con_cities = successors(current_city, city_visited)
        if len(con_cities) > 1:
            next_city = con_cities[0]
            for city in con_cities:
                if cost(city, cost_function) + get_distance(city[0], end_city) < \
                        cost(next_city, cost_function) + get_distance(next_city[0], end_city):
                    next_city = city

            result[0] = result[0] + 1
            result[1] = result[1] + next_city[1]
            result[2] = result[1] / next_city[2]
            result[3] = result[1] * next_city[2] * 0.000001
            city_visited.append(next_city[0])
            if next_city[0] == end_city:
                return result + city_visited
            fringe.append(next_city[0])

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
