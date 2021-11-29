# -*- coding: utf-8 -*-
from skimage.metrics import structural_similarity
import imutils
import cv2


def getScore(oldURL, newURL):
    """

    :param oldURL: 图片A
    :param newURL: 图片B
    :return: 1 相似
    """
    # 加载两张图片并将他们转换为灰度
    imageA = cv2.imread(oldURL)
    imageB = cv2.imread(newURL)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # 计算两个灰度图像之间的结构相似度指数
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    return score


def getDiffScoreAndDraw(oldURL, newURL):
    """

    :param oldURL: 图片A
    :param newURL: 图片B
    :return: 1 相似
    """
    # 加载两张图片并将他们转换为灰度
    imageA = cv2.imread(oldURL)
    imageB = cv2.imread(newURL)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # 计算两个灰度图像之间的结构相似度指数
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM:{}".format(score))

    # 找到不同点的轮廓以致于我们可以在被标识为“不同”的区域周围放置矩形
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1] if imutils.is_cv3() else cnts[0]
    # 找到一系列区域，在区域周围放置矩形
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    cv2.imshow("Modified", imageB)
    cv2.imwrite(r"D:\result.png", imageB)
    cv2.waitKey(0)
    return score


if __name__ == '__main__':
    saveURL = r"D:\testpyimg\test\\"
    saveURL_E = r".png"
    oldURL = saveURL + "tmpA" + saveURL_E
    newURL = saveURL + "tmpB" + saveURL_E
    # 加载两张图片并将他们转换为灰度  新加的注释
    getDiffScoreAndDraw(oldURL, newURL)
    # getDiffScoreAndDraw(newURL, oldURL)
