import csv

# 数据
names = ['小明', '小红', '小刚']
ages = [18, 20, 22]
genders = ['男', '女', '男']

# 创建CSV文件
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '年龄', '性别'])  # 写入表头
    writer.writerows(zip(names, ages, genders))  # 按列写入数据