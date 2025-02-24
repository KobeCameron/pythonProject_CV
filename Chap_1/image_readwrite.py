#!/usr/bin/env python3
# encoding:utf-8


import cv2 as cv

def main():

    # 读入图像
    im = cv.imread("lena.jpg")

    # 读入图像,同时转换为灰度图
    im_gray = cv.imread("lena.jpg", cv.IMREAD_GRAYSCALE)

    # 读入图像,同时将图像大小缩小为原始大小的1/2
    im_small = cv.imread("lena.jpg", cv.IMREAD_REDUCED_COLOR_2)
    # 将上面缩小的图像写入文件
    cv.imwrite("lena_small.jpg", im_small)

    # 显示图像
    cv.imshow("Lena", im)
    cv.imshow("Lena_Gray", im_gray)
    cv.imshow("Lena_small", im_small)

    cv.waitKey()
    cv.destroyAllWindows()
#
# 因为Python文件默认有9个参数，其中九包含了”__name__“参数
# 如果一个py文件作为当前执行文件，那么其”__name__“参数就设置为“__main__”
# 为了解决一个py文件作为模块import到另一个文件中，更好地调用里面的函数
# 那么下面语句内部的语句并不会执行
if __name__  == '__main__':
    main()
