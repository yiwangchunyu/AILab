import numpy as np
import pandas as pd
import config
def load_data():
    data = pd.read_excel(config.DATA_FILE, names=['id','x1','x2','x3','x4','x5','x6','x7','label'])
    data = data.set_index('id')
    label = data['label']
    data = data.drop(data.columns[6:8], axis=1, inplace=False)

    #归一化处理 max-min归一化
    data_norm = (data - data.min())/(data.max()-data.min())

    #类标处理为0,1
    label = label.replace(['红葡萄','白葡萄'],[0,1])

    #label[label['label'] == '白葡萄'] = 0
    print(data.head())
    # print(data_norm.head())
    #print(label.head())

    return data_norm,label

def distance(x1, x2):
    vec1 = np.array(x1)
    vec2 = np.array(x2)
    return np.linalg.norm(vec1 - vec2)

if __name__ == "__main__":
    data, label = load_data()
    print(data.loc[1:6,:])
    print(label.tolist())