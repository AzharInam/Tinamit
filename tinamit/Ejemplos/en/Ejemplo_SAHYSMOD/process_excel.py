import xlsxwriter
'''
This code is export python data in MS excel. 
During debugging mode if you want to import your data to see calculations or do some manual checks 
with data in array format no need to worry. Update file path of workbook.
It should be path of your computer hard drive, where you want to store your data.
Just stop your program (using debug) at point where you want to check your data.
Click on python consoler of debegging mode.
import process_excel
and then write process_excel.process_excel(excel filename, data array name)  
'''
def process_excel(Filename, array):
    """
    :param Filename: excel file name in string
    :param array: data array name
    :return:
    """
    workbook = xlsxwriter.Workbook('C:\Sahysmod\debugging_sheets\\'+ Filename +'.xlsx')
    var_list = [x for x,v in array.items()]
    for i in range(len(var_list)):
        worksheet = workbook.add_worksheet(var_list[i][:20])
        Data_list = (array[var_list[i]]).tolist()
        Data_list.insert(0,var_list[i])
        col = 0
        row = 0
        if len(Data_list)>3:
            for var in Data_list:
                worksheet.write(row, col, var)
                row += 1
        else:
            for i in range(len(Data_list)):
                if i == 0:
                    for var in Data_list:
                        worksheet.write(row, col, var)
                        row += 1
                        break
                else:
                    for var in Data_list[i]:
                        worksheet.write(row, col, var)
                        row += 1
                    col += 1
                    row = 1
    workbook.close()
