#!/usr/bin/env python
# encoding: utf-8

"""
    图片转字符画
    实验楼免费python课程
    2019/03/22
    王雨晨
"""


# 导入pillow 的 Image 模块
from PIL import Image
import argparse


# 首先 构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument("file")  #输入文件
parser.add_argument("-o", "--output")  #输出文件
parser.add_argument("--width", type = int, default = 80)  #输出字符画宽
parser.add_argument("--height", type = int, default = 80) #输出字符画高

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file

# 输出字符画的宽度
WIDTH = args.width

# 输出字符画的高度
HEIGHT = args.height

# 输出字符画的路径
OUTPUT = args.output

# 定义 ascii 字符集，共70个字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# RGB 转字符函数
def get_char(r, g, b, alpha = 256):
    """
        将RGB 灰度值映射到字符列表中
    """
    # 判断 alpha 值
    if alpha == 0:
        return " "

    # 获取字符集的长度，这里为 70
    length =  len(ascii_char)

    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行处理，将灰度值映射到指定字符上
    unit = (256.0 + 1) / length

    # 返回灰度值对映的字符
    return ascii_char[int(gray/unit)]

if __name__ == "__main__":
    
    # 首先使用PIL的 Image.open 打开图片文件，获得对象 im
    im = Image.open(IMG)
    # 使用 PIL 库的 im.resize() 调整图片大小 NEAREST 表示低质量的图片
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    
    # 初始化输出的字符串
    txt = ""

    # 遍历图片每一行
    for i in range(HEIGHT):
        # 遍历图片每一行
        for j in range(WIDTH):
            # 将 (j, i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j,i)))

        # 遍历完一行后需要增加换行
        txt += "\n"
    # 打印转换后的字符画
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, "w") as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)
