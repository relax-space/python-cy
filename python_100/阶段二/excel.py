import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

def HandleMergedCell(sheet,cell_index):
    merge = sheet.merged_cells
    for rlow,rhigh,clow,chigh in merge:
            if cell_index[0] >= rlow and cell_index[0] < rhigh:
                if cell_index[1] >= clow and cell_index[1] < chigh:
                    cell_index = (rlow,clow)

    return cell_index

def HandleCellValue(book,sheet,cell_index):
    cell_type = sheet.cell_type(cell_index[0],cell_index[1])
    if cell_type == 4:
        value = bool(sheet.cell_value(cell_index[0],cell_index[1]))
        return value
    elif cell_type == 5:
        value = 'Error'
        return value
    elif cell_type == 3:
        date = datetime(*xldate_as_tuple(sheet.cell_value(cell_index[0],cell_index[1]),book.datemode))
        date = date.strftime('%Y-%m-%d')
        return date
    else:
        value = sheet.cell_value(cell_index[0],cell_index[1])
        return value


class ReadExcel():
    # 读取单个sheet的内容
    def __init__(self,filepath):
        self.book = xlrd.open_workbook(filepath)

    @property
    def getSheet(self):
        sheet_name = self.book.sheet_names()
        self.sheet = self.book.sheet_by_name(sheet_name[0])

        return self.sheet

    def getSheetValue(self):
        total_row = self.getSheet.nrows
        total_col = self.getSheet.ncols

        total_cell = []
        for x in range(total_row):
            for y in range(total_col):
                total_cell.append((x,y))
        handle_cell = []
        for cell in total_cell:
            handle_cell.append(HandleMergedCell(self.getSheet,cell))

        # print(handle_cell)
        value_list = []
        for cell in handle_cell:
            # value_list.append(HandleCellValue(self.book,self.getSheet,cell))
            value_list.append({cell:HandleCellValue(self.book,self.getSheet,cell)})
        print(value_list)

ReadExcel('./stu.xlsx').getSheetValue()



