# -*- coding: utf-8 -*-
# @Date  : 2020/5/21
# @Author: Luokun
# @Email : olooook@outlook.com

import random

import numpy as np


class KMeans:
    """
    K-means clustering(K均值聚类)
    """

    def __init__(self, k: int, eps: float = 1e-3, iterations=100):
        """
        :param k: 聚类类别数
        :param eps: 迭代停止条件
        :param iterations: 迭代最大次数
        """
        self.k, self.eps, self.iterations = k, eps, iterations
        self.centers = None  # 中心点

    def predict(self, X: np.ndarray):
        Y = np.zeros([len(X)], dtype=int)  # 预测值
        self.centers = X[random.sample(range(len(X)), self.k)]  # 随机选择k个点作为中心点
        for _ in range(self.iterations):
            for i, x in enumerate(X):
                # 更新每一个点所属的类别为离该点最近的中心点所在的索引
                Y[i] = np.linalg.norm(self.centers - x, axis=1).argmax()
            means = np.empty_like(self.centers)  # 各类别点的均值
            for i in range(self.k):
                if np.any(Y == i):  # 存在元素属于类别i
                    means[i] = np.mean(X[Y == i], axis=0)  # 计算类别i所有点的均值
                else:  # 不存在任何元素属于类别i
                    means[i] = X[np.random.randint(0, len(X))]  # 随计选择一个点作为类别i的均值
            if np.max(np.abs(self.centers - means)) < self.eps:
                break  # 中心点最大更新值小于eps,推出迭代
            self.centers = means  # 将更新后的均值作为各类别中心点
        return Y
