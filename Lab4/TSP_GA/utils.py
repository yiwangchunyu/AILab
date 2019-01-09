import math
def distance(pos1, pos2):
    #print(pos1, pos2)
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

def get_adaptive_score(sequence, data):
    return 1/get_distance_all(sequence, data)

def get_distance_all(sequence, data):
    total = 0
    for i in range(len(sequence) - 1):
        total += distance(data[sequence[i]], data[sequence[i + 1]], )
    return total

if __name__ == '__main__':
    print('utils main')