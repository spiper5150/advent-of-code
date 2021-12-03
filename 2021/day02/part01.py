from entities import Submarine

def get_data():
    with open('input.txt') as file: 
        return file.readlines()

def move_submarine(sub: Submarine, direction: str, value: int):
    if(direction == 'up'):
        sub.depth = sub.depth - value
    elif(direction == 'down'):
        sub.depth = sub.depth + value
    else:
        sub.position = sub.position + value
    pass

def solution(data):
    sub = Submarine()
    for x in data:
        [direction, value] = x.strip().split(' ')
        move_submarine(sub, direction, int(value))
    
    return sub.coordinates

print(solution(get_data()))
