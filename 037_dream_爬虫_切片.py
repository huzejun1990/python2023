# @Author : huzejun
# @Time : 2023/1/13 0:11

s = 'hello world'

# 在切片中直接写一个下标
print(s[0])

# 左闭右开区间  包含坐标的数据 不包含右边的数据
print(s[0:4])

# 是从起始的值开始 一直到末尾
print(s[1:])

# 是下标为0的索引的元素开始 一直到第二参数为止  遵循左闭右开区间
print(s[:4])

# hello world
# 从下标为0的位置开始 到下标为6的位置结束 每次增长2个长度
print(s[0:6:2])