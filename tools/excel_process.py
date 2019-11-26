# encoding=utf-8

"""
    功能：处理Excel文件，将第一列相同的行汇总放在新的Excel中
    版本：1.0
    作者：王雨晨
    日期：2019/2/28
"""

import xlrd  # 导入 excel 读模块
import xlwt  # 导入 excel 写模块


def main():

    f_name = input("请输入带后缀的文件名（例如:汇总.xls）：")

    # 调用excel读函数，读取文件内容
    workbook = excel_open(f_name)

    # 处理异常
    if not isinstance(workbook, xlrd.book.Book):
        print("文件名错误，不能识别文件，已退出")
    else:
        print("文件名正确，正在处理")

        # 将 第一个sheet 的数据传给 table
        table = workbook.sheets()[0]

        # 获取行数
        number_rows = table.nrows

        # 获取标题行
        title_row = table.row_values(0)
        # 将数据整理成列表格式
        data = []
        for i in range(1, number_rows):  # 从1开始，不需要标题行
            data.append(table.row_values(i))

        # 去除标题行后，对第一列去重，保存为名字数组
        new_filename = list(set(table.col_values(0)[1:]))

        # 创建字典，把数据整理下，key为新文件名，值为要写入的数据{filename1:[[title],[]]..}
        dict = {}
        for i in new_filename:
            data_list = [title_row]
            for j in range(len(data)):
                if data[j][0] == i:
                    data_list.append(data[j])
            dict[i] = data_list

        # 调用函数 将相同行汇总后的数据写入Excel
        for key, value in dict.items():
            excel_write(key, value)

        print("已完成处理")

def excel_open(filename):
    """
        读取excel，返回表数据
    """

    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception as e:
        print(str(e))


def excel_write(filename, value):
    """
        函数功能 ，将数据写入excel中
    """
    workbook = xlwt.Workbook(encoding='gbk')
    worksheet = workbook.add_sheet(filename)

    # 将 value 内容写入单元格
    for i in range(len(value)):
        for j in range(len(value[i])):
            worksheet.write(i,j,value[i][j])

    workbook.save(filename+'.xls')


if __name__ == main():
    main()