from entities import Submarine

def get_data():
    with open('input.txt') as file: 
        return file.readlines()

def move_submarine(sub: Submarine, direction: str, value: int):
    if(direction == 'up'):
        sub.aim = sub.aim - value
    elif(direction == 'down'):
        sub.aim = sub.aim + value
    else:
        sub.position = sub.position + value
        sub.depth = sub.depth + (sub.aim * value)
    pass

def solution(data):
    sub = Submarine()
    for x in data:
        [direction, value] = x.strip().split(' ')
        move_submarine(sub, direction, int(value))
    
    return sub.coordinates
    
print(solution(get_data()))

