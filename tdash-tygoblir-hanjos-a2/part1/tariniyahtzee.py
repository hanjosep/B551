import sys
from queue import PriorityQueue
def calculate_expected_value(d1, d2, d3, i, j, k):
    expected_value = 0
    for m in range(1, 7):
        if i:
            d1 = m  # roll a dice and return in between 1 and 6
        else:
            d1 = d1  # No roll.return original value
        for n in range(1, 7):
            if j:
                d2 = n
            else:
                d2 = d2
            for o in range(1, 7):
                if k:
                    d3 = o
                else:
                    d3 = d3
                expected_value += (d1/6 + d2/6 + d3/6)
                # expected_value += 1 / 6 * (d1 + d2 + d3)  # probability of each side of roll is 1/6
    return expected_value
def roll_a_dice(d1, d2, d3):
    expected_value = PriorityQueue()
    for i in [True, False]:  # rolling dice 1
        for j in [True, False]:  # rolling dice 2
            for k in [True, False]:
                expected_value.put((- calculate_expected_value(d1, d2, d3, i, j, k), [i, j, k]))
    return expected_value.get()  # return the max value from the queue
# The main function
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise (Exception("Error: Please enter agrs in format dice1 value,dice2 value and dice3 value"))
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    if a < 1 or a > 6 or b < 1 or b > 6 or c < 1 or c  > 6:
        sys.exit()
    else:
        if a == b == c:
            print("You got max point.End of Game")
        else:
            result = roll_a_dice(a, b, c)
            print(result)
            if result[1][0]:
                print("Roll the first dice")
            if result[1][1]:
                print("Roll the second dice")
            if result[1][2]:
                print("Roll the third dice")