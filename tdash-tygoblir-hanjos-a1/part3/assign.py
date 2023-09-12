#!/usr/local/bin/python3

# put your group assignment program here!
import random
import sys


def readfile(inputfile):
    userdict = {}
    with open(inputfile, 'r') as file:
        for line in file:
            x = line.rstrip("\n").split(" ")

            preference = [x[1], x[2]]
            userdict[x[0]] = preference
        return userdict


def cost(succ, k, m, n, sizedict, denydict, requestdict):
    group_total = len(succ)

    size_complain = 0
    request_complain = 0
    deny_complain = 0
    # print(denydict)
    # print(requestdict)
    for team in succ:
        # print(team)
        for member in team:
            # print(member)
            # print(team)
            if len(team) != sizedict[member]:
                size_complain += 1
            denylist = denydict[member].split(',')
            for y in denylist:
                # print(y)
                if y in team:
                    deny_complain += 1
            # print(requestdict[member])
            for z in requestdict[member]:
                if z not in team and z != 'xxx':
                    request_complain += 1

    # print(size_complain)
    # print(deny_complain)
    # print(request_complain)

    totalcost = (int(k) * group_total) + size_complain + (int(n) * request_complain) + (int(m) * deny_complain)
    return totalcost


def successor1(currentteams, k, m, n, sizedict, denydict, requestdict):
    costnow = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
    lowestcost = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
    finalteam = currentteams
    for j in range(5000):
        lowestcost = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
        startteams = []
        for i in currentteams:
            startteams.append(i)
        for q in range(len(startteams) * 3):
            lowestcost = cost(startteams, k, m, n, sizedict, denydict, requestdict)
            newteams = []
            for ateam in startteams:
                newteams.append(ateam)
            team1 = random.choice(startteams)
            team2 = random.choice(startteams)
            if team1 != team2 and len(team1) + len(team2) <= 3:
                newteam = team1 + team2
                newteams.remove(team1)
                newteams.remove(team2)
                newteams.append(newteam)
                costcurrent = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
                costnew = cost(newteams, k, m, n, sizedict, denydict, requestdict)
                if costcurrent > costnew:
                    currentteams = newteams
                    costnow = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
            else:
                costnow = cost(currentteams, k, m, n, sizedict, denydict, requestdict)
        if costnow < lowestcost:
            lowestcost = costnow
            finalteam = []
            for p in currentteams:
                finalteam.append(p)
    return (finalteam, lowestcost)



# def main():
if __name__ == "__main__":
    k = sys.argv[2]
    m = sys.argv[3]
    n = sys.argv[4]
    userdict = readfile(sys.argv[1])
    requestdict = {}
    denydict = {}
    sizedict = {}

    for i in userdict:
        counter = 0
        for j in userdict[i]:
            if counter == 0:
                requestdict[i] = j
            if counter == 1:
                denydict[i] = j
            counter += 1
    for i in requestdict:
        string = requestdict[i]
        list1 = string.split('-')
        total = len(list1)
        sizedict[i] = total
        requestdict[i] = list1

    # print(requestdict)
    # print(denydict)
    # print(sizedict)

    startteams = []

    for i in userdict:
        teamlist = [i]
        startteams.append(teamlist)
    lowestcost = cost(startteams, k, m, n, sizedict, denydict, requestdict) + 1
    finalteam = startteams
    for i in range(50):
        team = successor1(startteams, k, m, n, sizedict, denydict, requestdict)[0]
        lowcost = successor1(startteams, k, m, n, sizedict, denydict, requestdict)[1]
        if lowcost < lowestcost:
            lowestcost = lowcost
            finalteam = []
            for item in team:
                finalteam.append(item)
            print('The teams are:')
            teamcounter = 1
            for team in finalteam:
                string1 = ('team{teamnum}: ')
                counter = 0
                for person in team:
                    if counter == 0:
                        string1 = string1 + str(person)
                        counter += 1
                    else:
                        string1 = string1 + '-' + str(person)
                print(string1.format(teamnum=teamcounter))
                teamcounter += 1
            print('at a cost of', lowestcost, 'minutes')



# main()