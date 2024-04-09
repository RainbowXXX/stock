import pandas as pd
from datetime import datetime
df = pd.read_csv('output_result.csv', encoding='gbk')

df.replace(0,'', inplace=True)


df.to_csv('f_output_result.csv', index=False, encoding='gbk')
# # 读取CSV文件
# df = pd.read_csv('result.csv', encoding='gbk')

# df.fillna(0, inplace=True)

# # 对每一行进行操作
# for index, row in df.iterrows():
#     # 获取第3列到第33列的数据
#     data = row.iloc[4:33]
    
#     # 找到最大值及其对应的列索引
#     max_value = data.max()
#     max_index = data.idxmax()
    
#     # 获取对应的表头数据
#     column_headers = df.columns.tolist()
    
#     # 获取最大值对应的表头数据
#     max_value_header = column_headers[column_headers.index(max_index)]
    
#     # 获取第34列到最后一列的数据
#     data_end = row.iloc[33:]
    
#     # 找到再次出现最大值时对应的列索引（从第34列到最后一列）
#     max_value_indexes_end = [i for i, value in enumerate(data_end) if value >= max_value]
    
#     # 获取对应的表头数据
#     max_value_indexes_headers_end = [column_headers[i + 33] for i in max_value_indexes_end]
    
#     # 将得到的数据写入到对应行的最后一列
#     df.iloc[index, -1] = max_value_indexes_headers_end[0] if max_value_indexes_headers_end else ''

#     max_value_time = datetime.strptime(max_value_header, '%Y/%m/%d')  # 假设时间格式为'YYYY-MM-DD HH:MM:SS'

#     # 获取最后一列的时间数据
#     try:
#         last_column_time = datetime.strptime(df.iloc[index, -1], '%Y/%m/%d')  # 假设时间格式为'YYYY-MM-DD HH:MM:SS'

#         # 计算时间差
#         time_difference = last_column_time - max_value_time

#         # 将时间差保存在最后一列
#         df.loc[index, df.columns[-1]] = str(time_difference)
#     except:
#         continue


# # 将修改后的数据写入到CSV文件中
# df.to_csv('output_result.csv', index=False, encoding='gbk')



