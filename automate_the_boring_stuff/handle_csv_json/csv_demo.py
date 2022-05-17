import csv
"""
csv

"""

# 处理包含列标题行的CSV文件，使用DictReader DictWriter（使用csv文件的第一行作为这些字典的键）
# with open('计算机软件工程考公1.CSV') as exampleFile:
#     exampleDictReader = csv.DictReader(exampleFile)
#     for row in exampleDictReader:
#         print(row['职位名称'], row['岗位描述'])
with open('output_title.csv', 'w', newline='') as outputFile:
    outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Sex', 'Age'])
    outputDictWriter.writeheader()
    outputDictWriter.writerow({'Name': 'yinlei', 'Sex': 'male', 'Age': '23'})




# with open('new_csv.csv', 'w', newline='',) as outputFile:
#     outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
#     outputWriter.writerow(['yin', 'lei', 'like', 'chen', 'shuang'])


# with open('计算机软件工程考公1.CSV') as exampleFile:
#     exampleReader = csv.reader(exampleFile)
#     for row in exampleReader:# reader对象只能循环一次，要再次读取csv文件必须调用csv.reader来创建一个对象
#         print(f'Row #{exampleReader.line_num} {row}')
#     # exampleData = list(exampleReader)
#     # print(exampleData)
#     # print(exampleData[0][1])

