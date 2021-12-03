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

def part1(data):
    sub = Submarine()
    for x in data:
        x = x.strip().split(' ')
        direction = x[0]
        value = int(x[1])
        move_submarine(sub, direction, value)
    
    return sub.coordinates

def part2(data):
    pass

def main():
    print(part1(get_data()))
    print(part2(get_data()))
    pass

main()