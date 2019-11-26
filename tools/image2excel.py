"""
    EXCEL像素画
    打开图片，生成EXCEL的像素画
"""

from PIL import Image
import xlsxwriter


def write_image_to_excel(fimage, fname):
    """
        打开图片，将每个像素的颜色值RGB值写入excel中
    """
    # 打开图片，同时将图片 Mode 转为 RGB 模式
    img = Image.open(fimage).convert('RGB')
    # 获取图片的大小，
    img_width, img_height = img.size[0], img.size[1]
    # 如果图片太大 ，超过了EXCEL的格数，上报异常
    if img_width > 1048576 or img_height > 16384:  # xlsxwriter max dim
        raise Exception("too large image")
    # 实例化 excel
    book = xlsxwriter.Workbook("{}.xlsx".format(fname))
    sheet = book.add_worksheet("image")
    # 获取像素值，并写入 excel 的格中
    pixel = img.load()
    for r in range(0, img_height):
        for c in range(0, img_width):
            fmt = book.add_format({'pattern': 1, 'bg_color':
                "#{:02x}{:02x}{:02x}".format(pixel[c, r][0],
                                             pixel[c, r][1],
                                             pixel[c, r][2])})
            sheet.write(r, c, None, fmt)
    # 设置单元格为方型
    col_width = 1
    row_height = col_width * 10
    for r in range(0, img_height):
        sheet.set_row(r, row_height)
    sheet.set_column(0, img_width, col_width)

    book.close()


def main():
    """
        主函数
    """
    write_image_to_excel("lena.jpg", "lena")


if __name__ == '__main__':
    main()
