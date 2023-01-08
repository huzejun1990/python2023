# @Author : huzejun
# @Time : 2023/1/8 16:50

# 转换为整型
# str --> int
# a = '123'
# print(type(a))
# b = int(a)
# print(type(b))

# float --> int
# a = 1.63
# print(type(a))
# # 如果我们将float转换为整数，那会返回的是小数点前面的数据
# b = int(a)
# print(b)
# print(type(b))

# boolean --> int
# 强制类型转换为谁，就写什么方法
# a = False
# print(type(a))
# b = int(a)
# # true --> 1
# print(b)
# print(type(b))

# 123.45 和 12ab 字符串，都包含非法字符，不能被转换成整数，会报错
# 以下 如果字符串当中包含了非法的 则报错
# a = '1.23'
# print(type(a))
# b = int(a)
# print(b)

a = '12ab'
print(type(a))
b = int(a)
print(b)
