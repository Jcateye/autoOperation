# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

import aircv as ac
import pytesseract
from PIL import Image
import pyautogui as ui

import executor
import parse_excel
from find import find

screenshot_path = r'E:\picture\test.png'
threshold = 0.8
duration = 0.1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test():
    b = ui.alert(text='开始程序吗?', title='提示', button='ok', timeout=1000)
    print(b)
    x, y = ui.position()
    print(x, y)
    ui.move(200, 200, duration=1)
    print(ui.position())
    # ui.press(['num0', 'num1', 'num2', 'num3', 'num4', 'enter'])
    # width, height = ui.size()
    # ui.moveTo(width - 2, height - 20, duration=0.3)
    # ui.click()
    # time.sleep(1)

    # ui.hotkey('win', 'd')
    im = ui.screenshot(r'E:\picture\test.png')
    mouse_click_picture(path=r'E:\picture\welink.png')
    time.sleep(1)
    mouse_click_picture(r'E:\picture\chat.png', False)
    time.sleep(1)
    ui.press(input_pinyin('queshi'))


def mouse_click_picture(path, duubleClick=True):
    # img = Image.open('E:\picture\chat.png')
    # text = pytesseract.image_to_string(img)
    # print('text is: ', text)
    ui.screenshot(screenshot_path)

    positionList = find(screenshot_path, path, threshold)
    # os.remove(screenshot_path)
    print(path)
    for pos in positionList:
        print(pos)
        ui.moveTo(x=int(pos[0]), y=int(pos[1]), duration=duration)
        if duubleClick:
            ui.doubleClick()
        else:
            ui.click()
    # outlookLocate = ui.locateCenterOnScreen(path, grayscale=True)
    # print('picture position ----', path, outlookLocate, type(outlookLocate))
    # ui.moveTo(outlookLocate, duration=0.5)


def input_pinyin(input):
    inputList = list(input)
    print(inputList)
    inputList.append('space')
    inputList.append('enter')
    return inputList


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    dic = parse_excel.read()
    print(dic)
    # 表
    count1 = 0
    for (key, stepList) in dic.items():
        count1 += 1
        print(f'第{count1}张表,开始执行自动化流程........')
        # ui.hotkey('win', 'd')
        # 行
        count2 = 0
        for list in stepList:
            count2 += 1
            print(f'第{count2}行,开始执行........')
            # 列
            count3 = 0
            for op in sorted(list, key=lambda operation: operation.order):
                count3 += 1
                print(f'---第{count2}行, 第{count3}次,开始执行........')
                executor.execute(op)
                print(f'---第{count2}行,第{count3}次,结束执行........')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
