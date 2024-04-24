import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\DDF1.xlsx')
sh = wb['Sheet2']

for r in range(1,5):
    for c  in range(1,3):

        sh.cell(row=r,column=c).value='Pass'

print('Written successfully')

wb.save('C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\DDF1.xlsx')