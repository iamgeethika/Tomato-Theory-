from main import *

def rule3(cell_value:int, neighbors) -> int:
    if (neighbors[0]==1 or neighbors[2]==1):
        return 1
    return cell_value

