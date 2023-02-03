import os
import xlsxwriter

def get_size_in_mb(file_path):
    return round(os.path.getsize(file_path) / (1024 * 1024), 2)

with open("file_paths.txt", "r") as f:
    file_paths = f.readlines()

workbook = xlsxwriter.Workbook("file_sizes.xlsx")
worksheet = workbook.add_worksheet()

row = 0
col = 0
worksheet.write(row, col, "File Path")
worksheet.write(row, col + 1, "Size (MB)")
row += 1

for file_path in file_paths:
    file_path = file_path.strip()
    size_in_mb = get_size_in_mb(file_path)
    worksheet.write(row, col, file_path)
    worksheet.write(row, col + 1, size_in_mb)
    row += 1

workbook.close()
