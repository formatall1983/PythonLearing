import xlrd
import os

path = os.getcwd()
path = path+os.sep+'学习用.xlsx'
xlsx=xlrd.open_workbook(path)
table=xlsx.sheet_by_name('重新建立')
table=xlsx.sheet_by_index(0)
print(table.cell_value(5,3))
print(table.cell(5,3).value)
print(table.row(5)[3].value)


import xlwt

