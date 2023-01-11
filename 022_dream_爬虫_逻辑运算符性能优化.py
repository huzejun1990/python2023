# @Author : huzejun
# @Time : 2023/1/11 17:58

# and的性能优化
# a = 36
# a > 10 and print('hello world')
# and性能优化，当and前面的结果为false的情况下，那么后面的代码就不再执行了
# a < 10 and print('hello world')

# or 的性能优化
a = 38

# a > 39 or print('你好世界！')
a > 37 or print('你好，世界')

# and 短路与
# or 短路或