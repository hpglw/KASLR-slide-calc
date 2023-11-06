import re

with open('memmap.txt', encoding='utf-16') as f:
    content = f.read()

pattern = re.compile(r'Available\s+(\w+)-')

starts = []
for m in pattern.findall(content):
    starts.append(m)

hex_starts = []  # 存储16进制值的列表

for start in starts:
    decimal_start = int(start, 16)  # 将16进制字符串转换为10进制整数
    modified_value = (decimal_start - 0x100000) / 0x200000  # 执行减法和除法操作
    hex_starts.append(hex(int(modified_value)))  # 将结果转换为16进制字符串并添加到列表中

octal_starts = []  # 存储8进制值的列表

for hex_value in hex_starts:
    decimal_value = int(hex_value, 16)  # 将16进制字符串转换为10进制整数
    octal_value = oct(decimal_value).lstrip('0o')  # 将10进制整数转换为8进制字符串，并移除 '0o' 前缀
    octal_value = octal_value.zfill(1)  # 填充为1位八进制，保留原本为0的值
    if int(octal_value, 8) <= 256:  # 仅输出小于等于256的值
        octal_starts.append(octal_value)

# 将结果写入文件 'slide=.txt'
with open('slide=.txt', 'w') as slide_file:
    for octal_value in octal_starts:
        slide_file.write(octal_value + '\n')
