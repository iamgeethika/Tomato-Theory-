from main import *

def rule2(cell_value:int, neighbors) -> int:
    c = 0
    for i in range(0,8):
        if(neighbors[i] == 1):
            c = c + 1


    if(cell_value == 0 and c == 3):
        return 1

    elif(cell_value == 1 and c == 2):
        return 1

    elif(cell_value == 1 and c == 3):
        return 1

    elif((c == 0 or c == 1 or c >= 4)):
        return 0

    else:
        return 0

