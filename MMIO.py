import re

with open('memmap.txt', encoding='utf-16') as f:
    content = f.read()

pattern = re.compile(r'MMIO       (\w+)-')

mmio_values = []
for m in pattern.findall(content):
    mmio_values.append(int(m, 16))

# 转换为10进制并保存到文件
with open('MMIO.txt', 'w') as output_file:
    for mmio_value in mmio_values:
        decimal_value = int(mmio_value)
        output_file.write(str(decimal_value) + '\n')
