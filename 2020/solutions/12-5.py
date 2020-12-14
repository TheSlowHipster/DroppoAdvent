import numpy as np
import math



def makePlane():
    airplane = np.empty((128,8))
    seatID = 0
    for row in range(airplane.shape[0]):
        for seat in range(airplane.shape[1]):
            airplane[row][seat] = seatID
            seatID += 1
    return airplane

def decode(ticket):
    _rows = ticket[0:7]
    _columns = ticket[7:]

    row = int(rowDecode(_rows))
    col = seatDecode(_columns)

    return row, col
    
def rowDecode(rows):
    _max = 127
    _min = 0
    _mid = math.floor((_max + _min) / 2)
    i = 0
    ret = ""
    for i in range(len(rows)):
        if rows[i] == "F":
            ret+="0"
        elif rows[i] == "B":
            ret += "1"
    return int(ret,2)

def seatDecode(seats):
    switch ={
        "LLL": 0,
        "LLR": 1,
        "LRL": 2,
        "LRR": 3,
        "RLL": 4,
        "RLR": 5,
        "RRL": 6,
        "RRR": 7
    }
    # print(switch.get(seats))
    return switch.get(seats)

def problem1():
    _f = open("inputs/12-5-input")
    maxSeat = 0
    airplane = makePlane()
    for ticket in _f.read().splitlines():
        row, col = decode(ticket)
        tmp = airplane[row][col]
        if tmp >= maxSeat:
            maxSeat = tmp
    _f.close()
    return maxSeat

def problem2():
    yourSeat = 0
    airplane = makePlane()
    _f = open("inputs/12-5-input")
    for ticket in _f.read().splitlines():
        row, col = decode(ticket)
        airplane[row][col] = -1
    airplane = airplane.reshape((-1,))
    while yourSeat + 1 < airplane.shape[0]:
        # print(f'{airplane[yourSeat - 1]} : {airplane[yourSeat]} : {airplane[yourSeat + 1]}')
        if airplane[yourSeat - 1] == -1 and airplane[yourSeat + 1] == -1 and airplane[yourSeat] != -1:
            return yourSeat
        else:
            yourSeat += 1


    return yourSeat

print(problem1())
print(problem2())