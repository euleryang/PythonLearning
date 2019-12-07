'''
判断输入的边长是否构成三角形
如果构成三角形，则计算出面积

version: 0.1
Author: SamYang
Date: 2019-12-07

'''

import math

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

if a + b > c and b + c > a and c + a > b:
    perimeter = a + b + c
    print("周长 %.2f" % perimeter)

    half = perimeter / 2
    area = math.sqrt(half * ((perimeter  - a) * (perimeter  - b) * (perimeter  - c)))
    print("面积 %.2f" % area)
else:
    print("构不成三角形")