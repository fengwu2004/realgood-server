import pandas as pd

xls_file = pd.ExcelFile('/Users/yan/Desktop/SwClass.xlsx')

df = xls_file.parse('Sheet1')

print(df)