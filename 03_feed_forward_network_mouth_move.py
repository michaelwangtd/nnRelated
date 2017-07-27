# -*- coding:utf-8 -*-

import numpy as np

if __name__ == '__main__':

    np.set_printoptions(linewidth=800,suppress=True)

    '''
        查看X,Y的数据格式
    '''
    # 这里指定编码是二进制格式加载
    X = np.load('D:/workstation/repositories/nnRelated/data/X.npy',encoding='bytes')
    print(type(X))
    print(X.shape)
    # print(X)
    sampleNum = 0
    for arrItem in X:
        print('------------')
        print(arrItem.shape)
        print(type(arrItem))
        print(arrItem.shape[0])
        sampleNum = sampleNum + arrItem.shape[0]
        print(arrItem)
        # listItem = list(arrItem)
        # listItem = arrItem.tolist()
        # print(type(listItem))
        # print(len(listItem))
        # print(listItem)
    # print(sampleNum)

    # Y = np.load('D:/workstation/repositories/nnRelated/data/Y.npy', encoding='bytes')
    # print(type(Y))
    # print(Y.shape)
    # # print(X)
    # for arrItem in Y:
    #     print('--------')
    #     print(arrItem.shape)
    #     print(type(arrItem))
    #     print(arrItem)