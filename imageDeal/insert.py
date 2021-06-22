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
def insertWater(carrierPath, waterMarkPath, savePath, times=7, N=8):
    carrier = ReadAndWrite.readBmp(carrierPath)#'F:\pictures\owl-24.bmp'
    # N = 8
    blocks = CutAndStitch.cut(carrier, N)

    waterMark = ReadAndWrite.readBmp(waterMarkPath)#'F:\pictures\\SCU.bmp'
    w_width, w_height = waterMark.shape
    water_al = Arnold.Arnold(waterMark, 1, 1, times)
    # water_rec = Arnold.DeArnold(water_al, 1, 1, 7)
    i = 0
    j = 0
    inbeded_blocks = []
    for ori_lines in blocks:
        inbeded_lines = []
        for block in ori_lines:
            if (i < w_width) and (j < w_height):
                dct_subImg = DCT.dct(block)
                M = np.rint(dct_subImg / steps)
                if water_al[i][j] == 0:
                    M[4, 4] = np.floor(M[4, 4] / 2) * 2
                else:
                    M[4, 4] = np.floor(M[4, 4] / 2) * 2 + 1
                inbeded_block_dct = M * steps
                inbeded_block = DCT.Ddct(inbeded_block_dct)
                inbeded_lines.append(inbeded_block)
            else:
                inbeded_lines.append(block)
            j = j + 1
        i = i + 1
        j = 0
        inbeded_blocks.append(inbeded_lines)
    inbeded_img = CutAndStitch.stitch(inbeded_blocks)

    # print(np.max(dct_subImg))
    ReadAndWrite.writeBmp(np.rint(inbeded_img), savePath, 'RGB')#'F:\pictures\\result.bmp'
