from xlwt import *

w = Workbook()
ws = w.add_sheet('xlwt was here') #название листа
w.save('mini.xls') #название файла