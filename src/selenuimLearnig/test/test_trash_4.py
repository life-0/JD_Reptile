""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_trash_4.py 
 @Time : 2021/1/8 20:19
 TODO @desc: 测试线程池

"""

from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:  # 创建进程池
        print(p.map(f, [1, 2, 3, 10]))
# 将数组中的每个元素提取出来当作函数的参数，创建一个个进程，放进进程池中
# 第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入函数中
