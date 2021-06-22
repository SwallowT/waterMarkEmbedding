import numpy as np
import math
import cv2

i = 0
j = 0


def genA(N):
    # N:int 图像的长宽
    A = np.zeros((N, N), dtype=float)  # DCT正变换
    for i in range(N):
        for j in range(N):
            x = 0
            if i == 0:
                x = math.sqrt(1 / N)
            else:
                x = math.sqrt(2 / N)

            A[i][j] = x * np.cos((2 * j + 1) * math.pi * i / (2 * N))
    return A


def dct(f):
    # f:np.array 图像原始数据
    M, N = f.shape

    A = genA(N)

    temp = np.dot(A, f)
    result = np.dot(temp, A.T)
    return result


def Ddct(r):
    # r:np.array 图像DCT系数
    M, N = r.shape
    A = genA(N)

    temp = np.dot(A.T, r)
    result = np.dot(temp, A)
    return result
