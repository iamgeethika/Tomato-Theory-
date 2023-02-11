from main import *

def rule1(cell_value: int, neighbors) -> int:
    if(cell_value==1):
        return 1
    for i in range(0,8):
        if(i==7):
            if(neighbors[i] != 1):
                return 0

        elif(i!=7):
            if(neighbors[i] != 0):
                return 0

    return 1

