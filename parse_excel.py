import xlrd

from operation import operation

step_col = -1
picture_col = -1
click_col = -1
double_click_col = -1
content_col = -1
copy_col = -1
paste_col = -1
keyword_col = -1


def read():
    sheets = xlrd.open_workbook(r'E:\picture\步骤配置.xls')
    dic = dict()
    for sheet in sheets:
        print("--------开始解析表--------")
        paragraph_list = list()
        dic[sheet.name] = paragraph_list
        count = 0
        # 每行
        for rowIndex in range(sheet.nrows):
            step_list = list()
            paragraph_list.append(step_list)
            # 每列
            for colIndex in range(sheet.ncols):
                value = sheet.cell_value(rowIndex, colIndex)
                if rowIndex == 0:
                    map_title(colIndex, value)
                    continue
                # 列值映射到每个title
                count += 1
                op = map_column_value(colIndex, value, count)
                if op is not None:
                    step_list.append(op)
        print("--------结束解析表--------")
    return dic


# 图片	单击	双击	输入内容	复制	粘贴	键盘
def map_column_value(col, value, count):
    if value == "":
        return None
    op = operation(order=count, key="", loop=1)
    if col == step_col:
        pass
    elif col == picture_col:
        op.key = 'picture'
        op.value = value
        print(f'鼠标移动到{value}')
    elif click_col == col:
        op.key = 'click'
        op.loop = value
        print(f'单击{value}次')
    elif double_click_col == col:
        op.key = 'double_click'
        op.loop = value
        print(f'双击{value}次')
    elif content_col == col:
        op.key = 'content'
        op.value = value
        print(f'输入:{value}')
    elif copy_col == col:
        op.key = 'copy'
        op.loop = value
        print(f'复制当前文本:{value}次')
    elif paste_col == col:
        op.key = 'paste'
        op.loop = value
        print(f'粘贴:{value}次')
    elif keyword_col == col:
        op.key = 'keyword'
        op.loop = value
        print(f'按下键盘:{value}次')
    return op


# 图片	单击	双击	输入内容	复制	粘贴	键盘
def map_title(col, value):
    if value == "步骤":
        global step_col
        step_col = col
    elif value == "图片":
        global picture_col
        picture_col = col
    elif value == "单击":
        global click_col
        click_col = col
    elif value == "双击":
        global double_click_col
        double_click_col = col
    elif value == "输入内容":
        global content_col
        content_col = col
    elif value == "复制":
        global copy_col
        copy_col = col
    elif value == "粘贴":
        global paste_col
        paste_col = col
    elif value == "键盘":
        global keyword_col
        keyword_col = col


if __name__ == '__main__':
    read()
