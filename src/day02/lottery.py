"""
函数方法，因式分解，计算组合数

Version: 0.1
Author: SamYang
Date: 2019-12-07
"""

from random import randint, sample, randrange

#输出列表中的双色球号码
def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls):
            print('|', end=' ')
        print('%02d' % ball, end=' ')

    print()

# 随机选择一组号码
def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

def main():
    n = int(input("机选几注："))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()