import cv2
import numpy as np

import Arnold
import CutAndStitch
import DCT
import ReadAndWrite

steps = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                  [12, 12, 14, 19, 26, 58, 60, 55],
                  [14, 13, 16, 24, 40, 57, 69, 56],
                  [14, 17, 22, 29, 51, 87, 80, 62],
                  [18, 22, 37, 56, 68, 109, 103, 77],
                  [24, 35, 55, 64, 81, 104, 113, 92],
                  [49, 64, 78, 87, 103, 121, 120, 101],
                  [72, 92, 95, 98, 112, 100, 103, 99]])
def extractWater(inbededImgPath, w_width=64, w_height=64, times=7, N=8):
    watermark = np.zeros((w_width, w_height), dtype='bool')
    inbeded_img = ReadAndWrite.readBmp(inbededImgPath)# 'F:\pictures\\result.bmp'

    inbeded_blocks = CutAndStitch.cut(inbeded_img, N)

    i, j = 0, 0

    for i in range(w_width):
        for j in range(w_height):
            block_dct = DCT.dct(np.float32(inbeded_blocks[i][j]))
            temp = np.rint(block_dct / steps)
            if temp[4][4] % 2 == 0:
                watermark[i][j] = 0
            else:
                watermark[i][j] = 1
    watermark_DeAr = Arnold.DeArnold(watermark, 1, 1, times)
    ReadAndWrite.writeBmp(watermark_DeAr, 'F:\pictures\\rec_water.bmp', '1')
