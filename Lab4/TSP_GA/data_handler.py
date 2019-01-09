#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def load_data(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            curr_line = list(map(int, line[:-1].split(' ')))
            data.append(curr_line[1:])
    return data

def draw_map(data):
    data_arr = np.array(data)
    plt.scatter(x=data_arr[:,0], y=data_arr[:,1], s=5)
    plt.show()

def draw_path(sequence, data):
    data_arr = [data[pos] for pos in sequence]
    data_arr = np.array(data_arr)

    plt.figure('Path')
    ax=plt.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.scatter(x=data_arr[:, 0], y=data_arr[:, 1], s=5)
    ax.plot(data_arr[:,0],data_arr[:,1],c='r', linewidth=1, alpha=0.6)
    plt.show()

if __name__ == '__main__':
    data = load_data('data/cn144_location2.txt')
    print(len(data))
    #draw_map(data)
    sequence = [17, 19, 20, 16, 13, 5, 96, 100, 97, 50, 48, 55, 59, 54, 58, 57, 60, 56, 44, 47, 52, 51, 45, 46, 129, 131, 127, 135, 132, 122, 119, 117, 121, 120, 107, 106, 102, 112, 104, 101, 84, 77, 76, 73, 75, 1, 69, 68, 71, 67, 63, 64, 66, 22, 23, 30, 28, 32, 35, 38, 33, 37, 27, 29, 25, 21, 26, 24, 4, 0, 3, 7, 95, 10, 12, 42, 43, 15, 18, 11, 9, 8, 65, 61, 62, 70, 78, 79, 81, 72, 74, 80, 83, 87, 82, 115, 109, 110, 86, 108, 111, 133, 134, 128, 138, 137, 123, 125, 124, 118, 113, 143, 142, 116, 114, 89, 91, 92, 94, 93, 88, 90, 85, 99, 98, 105, 103, 39, 49, 53, 140, 141, 139, 136, 130, 126, 40, 41, 14, 2, 6, 31, 36, 34]
    #sequence = [42,15,98,104,106,107,103,113,87,111,109,108,112,136,133,134,135,131,132,128,127,130,41,40,47,46,54,49,52,53,48,45,57,61,56,60,55,59,58,142,141,140,137,129,139,138,124,123,120,126,125,118,122,121,110,116,119,114,144,143,117,115,90,83,91,89,92,93,95,94,77,75,74,76,2,70,69,72,68,71,79,80,78,82,73,81,84,88,86,85,102,105,100,99,101,97,63,62,66,64,65,67,23,24,31,32,37,35,36,39,34,20,18,38,28,33,29,30,26,22,27,25,7,5,9,3,1,4,8,6,96,11,13,44,14,12,10,21,17,19,16,51,50,43]
    #sequence = np.array(sequence)-1
    print(sequence)
    draw_path(sequence, data)
