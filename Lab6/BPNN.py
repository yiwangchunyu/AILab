import math
import numpy as np
import json
from sklearn.metrics import classification_report

import data_handler
import pyprind
import matplotlib.pyplot as plt


#把图片矩阵拉平
def get_flatten_norm(samples):
    #扁平化处理
    flat = np.array([sample.flatten() for sample in samples])
    #归一化
    norm = flat/256.0
    return norm


def get_act_sigmoid(x):
    act_vec = []
    for i in x:
        act_vec.append(1/(1+math.exp(-i)))
    act_vec = np.array(act_vec)
    return act_vec


def train(samples, labels, hiden_num=100):

    ################################################################################
    #配置神经网络
    sample_num = len(samples) #样本总数
    input_num = len(samples[0]) #输入层节点数
    output_num = 10 #输出层节点数
    hiden_num = hiden_num #隐藏层节点数
    # 输入层权重矩阵
    w1 = 0.2*np.random.random((input_num, hiden_num))-0.1
    #隐藏层权重矩阵
    w2 = 0.2 * np.random.random((hiden_num, output_num)) - 0.1
    #隐藏层偏置向量
    hiden_offset = np.zeros(hiden_num)
    #输出层偏置向量
    output_offset = np.zeros(output_num)
    #输入层权值学习率
    input_lrate = 0.3
    #隐藏层权值学习率
    hiden_lrate = 0.3
    #学习误差门限阈值
    err_threshold = 0.01
    ###############################################################################

    #训练神经网络
    ################################################################################
    print("training......")
    bar = pyprind.ProgPercent(sample_num)
    for index in range(0, sample_num):
        #print(index)
        #输出层真实值
        real_out = np.zeros(output_num)
        real_out[int(labels[index])] = 1

        #前向过程
        hiden_value = np.dot(samples[index],w1) + hiden_offset
        hiden_act = get_act_sigmoid(hiden_value)  #隐藏层激活值

        out_value = np.dot(hiden_act, w2) + output_offset
        out_act = get_act_sigmoid(out_value)

        #后向过程
        e = real_out - out_act  #误差值
        out_delta = e*out_act*(1-out_act)  #输出层delta
        hiden_delta = hiden_act*(1-hiden_act)*np.dot(w2, out_delta)  #隐藏层delta

        for i in range(0, output_num):#更新隐藏层到输出层权值
            w2[:,i] += hiden_lrate*out_delta[i]*hiden_act
        for i in range(0, hiden_num):#更新输入层到隐藏层权值
            w1[:,i] += input_lrate*hiden_delta[i]*samples[index]

        #输出层偏置更新
        output_offset += hiden_lrate*out_delta
        hiden_offset += input_lrate*hiden_delta

        bar.update()
    #将模型保存到文件

    save_network(input_num, hiden_num, output_num, output_offset, hiden_offset, w1, w2)

def save_network(input_num, hiden_num, output_num, output_offset, hiden_offset, w1, w2):

    network = {}
    network["input_num"]=input_num
    network["hiden_num"]=hiden_num
    network["output_num"]=output_num
    network["output_offset"] = output_offset.tolist()
    network["hiden_offset"] = hiden_offset.tolist()
    network["w1"]=w1.tolist()
    network["w2"]=w2.tolist()

    f = open("BPNetwork.model","w",encoding="utf-8")
    json.dump(network, f)
    f.close()
    print('saved....')

def predict(samples):
    network = json.load(open("BPNetwork.model","r"),encoding="utf-8")
    input_num = network["input_num"]
    hiden_num = network["hiden_num"]
    output_num = network["output_num"]
    hiden_offset = np.array(network["hiden_offset"])
    output_offset = np.array(network["output_offset"])
    w1 = np.array(network["w1"])
    w2 = np.array(network["w2"])

    result_labels = np.zeros(len(samples))

    for index in range(len(samples)):
        hiden_value = np.dot(samples[index], w1) + hiden_offset
        hiden_act = get_act_sigmoid(hiden_value)
        out_value = np.dot(hiden_act, w2) + output_offset
        out_act = get_act_sigmoid(out_value)
        result_labels[index] = np.argmax(out_act)

    return result_labels

if __name__ == "__main__":
    # 加载数据：训练集样本
    samples = data_handler.load_train_images()
    samples = get_flatten_norm(samples)
    # 加载数据：训练集类标
    labels = data_handler.load_train_labels()
    train(samples, labels, 100)

    #c测试集
    test_samples = data_handler.load_test_images()
    test_samples = get_flatten_norm(test_samples)
    test_labels = data_handler.load_test_labels()

    result_lables = predict(test_samples)
    #结果性能评估
    names = range(10)
    names = list(map(str, names))
    report = classification_report(test_labels, result_lables, target_names=names)
    print(report)
    with open("BPNetwork.model" + ".report", 'w') as tr:
        tr.write(report)

    #测试隐藏层节点数对准确率的影响
    # accuracy = []
    # bar= pyprind.ProgPercent(48)
    # for i in range(5,100,2):
    #     train(samples, labels, i)
    #     result_lables = predict(test_samples)
    #     acc = accuracy_score(test_labels, result_lables)
    #     accuracy.append([i,acc])
    #     bar.update()
    # accuracy = np.array(accuracy)
    # plt.plot(accuracy[:,0], accuracy[:,1])
    # plt.show()

