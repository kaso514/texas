from openpyxl import load_workbook
from datetime import datetime

# 1. 创建一场比赛
def create_match(database, small_blind=10, big_blind=20):
    workbook = load_workbook(database)
    worksheet = workbook.worksheets[2]
    max_row = worksheet.max_row
    worksheet.cell(max_row + 1, 1).value = max_row
    worksheet.cell(max_row + 1, 2).value = max_row
    worksheet.cell(max_row + 1, 3).value = datetime.now()
    worksheet.cell(max_row + 1, 4).value = small_blind
    worksheet.cell(max_row + 1, 5).value = big_blind
    workbook.save(database)
    workbook.close()
    message = "Match created success"
    return message

# 2. 基于每一手的结果更新比赛统计数据
# 2. 基于每一手的结果更新比赛统计数据


