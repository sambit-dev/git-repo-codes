import xlrd
excel_path1="QDB V6.0.xlsx"
excel_path2="QDB V7.0.xlsx"
# importing database
wb1 = xlrd.open_workbook(excel_path1)
wb2 = xlrd.open_workbook(excel_path2)
sheet1 = wb1.sheet_by_index(2)
sheet2 = wb2.sheet_by_index(2)
# cell comparision
for i in range(sheet1.nrows):
    for m in range(sheet1.ncols):
        if sheet1.cell_value(i,m)!=sheet2.cell_value(i,m):
            sheet1.cell_value(i, m)=(sheet1.cell_value(i, m),"-->",sheet2.cell_value(i,m))
