def get_data(file):
    with open(file) as file:
        random_numbers = file.readline().strip().split(',')
        cards = []

        for row in file.read()[1:].strip().splitlines():
            cards.append(row.split())

        return (random_numbers, cards)


def solution(data):

    return data


print('Test: ', solution(get_data('test-input.txt')))
#print('Answer: ', solution(get_data('input.txt')))
