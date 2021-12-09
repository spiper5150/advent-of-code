def get_data():
    with open('input.txt') as file:
        return file.read().splitlines()


def get_test_data():
    return ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def get_rating(data, binary, col, common):
    if(len(data) == 1):
        return data

    bit = list(binary)[col]
    if(bit == common):
        return binary


def get_common(array, get_max, tie):
    ones = 0
    zeros = 0

    for x in array:
        if(int(x) == 1):
            ones += 1
        else:
            zeros += 1

    if(ones == zeros):
        return tie

    if(get_max == True):
        return 1 if ones > zeros else 0
    else:
        return 1 if ones < zeros else 0


def get_bit_array(array, col):
    bit_array = []
    for x in array:
        bits = list(x)
        bit_array.append(bits[col])
    return bit_array


def solution(data):
    oxy_rating = data
    co2_rating = data
    for col in range(len(data[0])):
        oxyBitArray = get_bit_array(oxy_rating, col)
        co2BitArray = get_bit_array(co2_rating, col)

        epsilon = str(get_common(oxyBitArray, True, 1))
        gamma = str(get_common(co2BitArray, False, 0))

        oxy_rating = filter(lambda val: get_rating(
            oxy_rating, val, col, epsilon), oxy_rating)

        co2_rating = filter(lambda val: get_rating(
            co2_rating, val, col, gamma), co2_rating)

    return int(oxy_rating[0], 2) * int(co2_rating[0], 2)


print('Test: ', solution(get_test_data()))
print('Answer: ', solution(get_data()))
