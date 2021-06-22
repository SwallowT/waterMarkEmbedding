import numpy as np


def cut(origin, N):
    width, height = origin.shape

    m = int(width / N)  # 横向有m个8*8小块
    n = int(height / N)  # 纵向有n个8*8小块

    subImages = []
    for i in range(m):
        subImgline = []  # 一行的8*8小方块
        for j in range(n):
            subImg = origin[i * N: (i + 1) * N, j * N:(j + 1) * N]
            subImgline.append(subImg)
        subImages.append(subImgline)
    return subImages


def stitch(subImages):
    n = len(subImages)  # 纵向有n个8*8小块
    m = len(subImages[0])  # 横向有m个8*8小块

    allBlocks = []
    for i in range(n):
        tmpLine = []
        for j in range(m):
            tmpLine.append(subImages[i][j])
        img = np.concatenate(tmpLine, axis=1)
        allBlocks.append(img)
    reImg = np.vstack(allBlocks)
    return reImg
