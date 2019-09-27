import xlrd

from xlutils.copy import copy
from utils.pubilc import *
class OperationExcel:

    def getExcel(self):
        db = xlrd.open_workbook(data_dir('data','data.xls'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取Excel行数'''
        return self.getExcel().nrows

    def get_row_cel(self,row,col):
        '''获取单元格内容'''
        return self.getExcel().cell_value(row,col)

