import time

import pyautogui as ui
from find import find

screenshot_path = r'E:\picture\test.png'
threshold = 0.8
duration = 1


def execute(operation):
    if operation.key == "":
        return
    if operation.key == "picture":
        moveToCenter(operation.value)
        time.sleep(0.5)
        print(operation.value)
    elif operation.key == "click":
        print(f'click-----loop:{operation.loop}')
        for i in range(cover(operation.loop)):
            print(f'{operation.key}---{i}')
            ui.click()
    elif operation.key == "double_click":
        print(f'double_click-----loop:{operation.loop}')
        for i in range(cover(operation.loop)):
            print(f'{operation.key}---{i}')
            ui.doubleClick()
    elif operation.key == "content":
        print(operation.key)
        ui.press(input_pinyin(operation.value))
    elif operation.key == "copy":
        for i in range(cover(operation.loop)):
            print(operation.key)
            ui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            ui.hotkey('ctrl', 'c')
    elif operation.key == "paste":
        for i in range(cover(operation.loop)):
            print(operation.key)
            ui.hotkey('ctrl', 'v')
    elif operation.key == "keyword":
        print(operation.key)
        ui.press(str(operation.value).split(","))


def cover(value):
    if value == "":
        return 0
    else:
        return int(value)


def moveToCenter(path):
    ui.screenshot(screenshot_path)
    positionList = find(screenshot_path, path, threshold)
    for pos in positionList:
        print(f'{path}---{pos}')
        ui.moveTo(x=int(pos[0]), y=int(pos[1]), duration=duration)


def input_pinyin(input):
    inputList = list(input)
    print(inputList)
    inputList.append('space')
    inputList.append('enter')
    return inputList
