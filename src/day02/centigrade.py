"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

将氏温度转换为华氏温度
F = 1.8C + 32
C = (F -32)*10/18

Version: 0.1
Author: SamYang
Date: 2019-12-07
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

c = float(input('请输入摄氏温度: '))
f = 1.8 * c + 32
print('%.1f摄氏度 = %.1f华氏度' % (c, f))