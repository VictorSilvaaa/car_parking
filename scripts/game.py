from scripts.level1 import level1
from scripts.level2 import level2

result = False
def game(level=1):
    if level == 1:
        result = level1()
    elif level == 2:
        result = level2()
    
    return result