# @Author : huzejun
# @Time : 2023/1/13 21:23

# 使用函数来计算1和2的和

# def sum():
#     a = 1
#     b = 2
#     c = a + b
#     print(c)
#
# sum()

def sum(a,b):
    c = a + b
    print(c)

# 位置参数  按照位置一一对应的关系来传递参数
sum(1,2)

sum(100,200)


#关键字传参
sum(b = 200,a = 100)

#定义函数的时候 sum(a,b) 我们称 a 和 b 为形式参数 简称形参
#调用函数的时候 sum(1,2) 我们称 1 和 2 为实际参数 简称实参