import numpy as np

def Arnold(waterImg, a, b, time):
    M, N = waterImg.shape
    A = np.zeros([M, M])
    for i in range(time):
        for y in range(M):
            for x in range(N):
                x_ = (x + b * y) % M
                y_ = ((a * x) + (a * b + 1) * y) % M
                A[y_][x_] = waterImg[y][x]

        waterImg = A.copy()

    return waterImg.astype(bool)


def DeArnold(waterImg, a, b, time):
    M, N = waterImg.shape
    A = np.zeros([M, M])
    for i in range(time):
        for y in range(M):
            for x in range(N):
                x_ = ((a * b + 1) * x - b * y) % M
                y_ = (-a * x + y) % M

                A[y_][x_] = waterImg[y][x]

        waterImg = A.copy()
    return waterImg.astype(bool)