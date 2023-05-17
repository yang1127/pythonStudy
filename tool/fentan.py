# -*-coding:utf-8-*-
# 前置：A、B列输入课程原价
# 一次分摊，礼品卡/券分摊到每个课程的价值
# 二次分摊，礼品卡/券分摊到每个课程的价值
import openpyxl

def calculate_promotion(file_path):
    # 打开已有文件
    wb = openpyxl.load_workbook(file_path)

    # 获取活跃表对象
    sheet = wb.active

    # 获取单元格对应的 Cell 对象
    max_row = sheet.max_row
    # 列A所有对象
    columnA = sheet['A2':'A%d' % max_row]
    # 列B所有对象
    columnB = sheet['B2':'B%d' % max_row]

    # 一次，券/礼品卡的实际价值
    c2 = sheet['C2']
    card = c2.value

    # 二次，券/礼品卡的实际价值
    d2 = sheet['D2']
    account = d2.value

    # A、B列总和
    sum_A = 0
    sum_B = 0
    list_A = []
    list_B = []
    for column_cells in columnA:
        for cell in column_cells:
            sum_A = sum_A + cell.value
            list_A.append(cell.value)
    for column_cells in columnB:
        for cell in column_cells:
            sum_B = sum_B + cell.value
            list_B.append(cell.value)

    # A列分摊后
    list_A.sort()
    list_out = []
    for element in list_A:
        list_out.append(round((element * card / sum_A + 0.005), 2))
    # 最后一个兜底
    last = card - sum(list_out[0:len(list_out) - 1])
    list_out[-1] = round(last, 2)

    # B列分摊后
    list_B.sort()
    list_out2 = []
    # 小数保留2位 四舍五入
    for element in list_B:
        list_out2.append(round((element * account / sum_B), 2))
    # 最后一个兜底
    last = account - sum(list_out2[0:len(list_out2) - 1])
    list_out2[-1] = round(last, 2)

    print([list_out, list_out2])
    return [list_out, list_out2]

if __name__ == '__main__':
    calculate_promotion("test.xlsx")