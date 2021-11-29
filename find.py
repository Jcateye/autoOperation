import aircv as ac
import cv2 as cv



def draw_circle(img, pos, circle_radius, color, line_width):
    cv.circle(img, (int(pos[0]), int(pos[1])), circle_radius, color, line_width)


def showImg(img):
    cv.namedWindow("image")
    cv.imshow('image', img)
    cv.waitKey(10000)  # 显示 10000 ms 即 10s 后消失
    cv.destroyAllWindows()


def findAndShow(src, dest, threshold=0.5):
    """
    找到并显示
    :param src: 源路径
    :param dest: 目标路径
    :param threshold: 精度 1 最大 0.7-8 适中， 0.5模糊
    :return: 数组
    """
    imsrc = cv.imread(src)
    imobj = cv.imread(dest)
    # find the match position
    pos = ac.find_all_template(imsrc, imobj, threshold)
    print(pos)
    for item in pos:
        result = item['result']
        print(result)
        circle_radius = 50
        color = (0, 255, 0)
        width = 2
        draw_circle(imsrc, result, circle_radius, color, width)
    showImg(imsrc)
    return [item["result"] for item in pos]


def find(src, dest, threshold=0.5):
    """
    找到并显示
    :param src: 源路径
    :param dest: 目标路径
    :param threshold: 精度 1 最大 0.7-8 适中， 0.5模糊
    :return: 数组
    """
    imsrc = cv.imread(src)
    imobj = cv.imread(dest)
    # find the match position
    pos = ac.find_all_template(imsrc, imobj, threshold)
    return [item["result"] for item in pos]


if __name__ == "__main__":
    old = r'E:\picture\test.png'
    newUrl = r'E:\picture\outlook.png'

    findAndShow(old, newUrl, 0.8)
    print("-------------------华丽分割线----------------------")
