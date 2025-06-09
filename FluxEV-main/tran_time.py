import csv
from datetime import datetime

# 输入文件路径
input_file_path = 'IOPS-read-data.csv'
# 输出文件路径
output_file_path = 'IOPS-read-data.csv'

# 打开输入文件和输出文件
with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
    # 创建CSV阅读器和写入器
    reader = csv.DictReader(infile)
    fieldnames = ['timestamp', 'value', 'is_anomaly']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # 写入标题行
    writer.writeheader()

    # 逐行读取并处理时间戳
    for row in reader:
        # 解析时间戳
        datetime_obj = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
        # 转换为Unix时间戳
        unix_timestamp = datetime_obj.timestamp()
        # 写入新的时间戳和其他列
        writer.writerow({
            'timestamp': int(unix_timestamp),
            'value': row['value'],
            'is_anomaly': row['is_anomaly']
        })

print("时间戳转换完成，输出文件已保存至：", output_file_path)
