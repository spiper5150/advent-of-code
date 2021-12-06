def get_data():
    with open('input.txt') as file: 
        return file.read().splitlines()
    
def get_test_data():
    return ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

def solution(data):
    gamma= ""
    epsilon = ""

    for i in range(len(data[0])):
        bitArray = []
        for binary in data:
            bits = list(binary) 
            bitArray.append(bits[i])

        gamma += min(set(bitArray), key=bitArray.count)
        epsilon += max(set(bitArray), key=bitArray.count)
    
    return int(gamma, 2) * int(epsilon, 2)

print('Test: ', solution(get_test_data()))
print('Answer: ', solution(get_data()))