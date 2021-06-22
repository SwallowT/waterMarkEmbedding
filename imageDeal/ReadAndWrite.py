import numpy as np
from PIL import Image


def readBmp(path):
    with Image.open(path) as image:
        # 转换为灰度图片
        if image.mode == 'RGB':
            image = image.convert('L')
        image_data = np.array(image)
    return image_data


def writeBmp(image_data, savepath, mode):
    image = Image.fromarray(image_data)
    if image.mode == 'F':
        image = image.convert(mode)
    image.save(savepath)