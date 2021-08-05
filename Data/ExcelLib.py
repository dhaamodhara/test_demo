import xlrd
from Library import Config
#
# wb=xlrd.open_workbook("c:/users/Amaresh/Documents/objects.xlsx")
# ws=wb.sheet_by_name("login")
# rows=ws.get_rows()
# headers=next(rows) #skipping headers
# d={row[0].value: (row[1].value,row[2].value) for row in rows}
# print(d)
#
# #testdata
# wb=xlrd.open_workbook("c:/users/Amaresh/Documents/TestData.xlsx")
# ws=wb.sheet_by_name("Registration")
# rows=ws.get_rows()
# for index,row in enumerate(rows):
#     print(index)
#     print(row)
#     if not row[0].value=="test_01":
#         continue
#     headers=ws.row_values(index-1,start_colx=2)
#     print(headers)
#     break
def read_data(sheetname, testcase):
    """ Return a list with headers as a tuple and test data as a list of tuples
    headers() and test datais [(),()] because we need to pass this list into a 3rd party library called parameterized_class"""
    workbook=xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet=workbook.sheet_by_name(sheetname)
    temp_data=[]
    data=[]
    header=None
    r=worksheet.get_rows()
    for index,item in enumerate(r):
        if not item[0].value==testcase:
            continue
        headers=worksheet.row_values(index-1,start_colx=2) #reading headers
        headers=tuple(headers)
        break
    r=worksheet.get_rows() #re-initializing iterator
    for item in r:
        if item[0].value == testcase:
            temp_data.append(tuple([temp.value for temp in item])[1:])
    for d in temp_data:
        if d[0].upper() == 'YES':
            data.append(d[1:])
    return [headers, data]
def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    r = worksheet.get_rows()
    next(r)     # Skip Headers
    return {item[0].value: (item[1].value, item[2].value) for item in r}


def get_modules_to_execute():
    workbook = xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet = workbook.sheet_by_name('Index')
    r = worksheet.get_rows()
    next(r)  # skip headers
    final = []
    for row in r:
        if row[1].value.upper() == 'YES':
            worksheet = workbook.sheet_by_name(row[0].value)
            tests = worksheet.get_rows()
            toRun = list(set([str(test[0].value) + '.py' for test in tests if not test[0].value == 'TestCase' and test[0].value]))
            final += [*toRun]
    return final


wb=xlrd.open_workbook(file path)
row=wb.sheet_by_name("sheetname")
for i in row print(row)
