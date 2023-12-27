from openpyxl import load_workbook

# 1. 获取用户信息，标记用户位置
workbook = load_workbook(database)
worksheet = workbook.worksheets[1]

# 1.1 逐个询问用户是否参与本场比赛
# 2. 下注（翻前）
# 3. 生成扑克，洗牌，
# 4. 发牌
# 4. 下注（翻后）
# 5. 发牌
# 6. 下注（转牌）
# 7. 发牌
# 8. 下注（河牌）
# 9. 牌力比较
# 10. 更新数据