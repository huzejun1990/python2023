# @Author : huzejun
# @Time : 2023/1/8 18:47

# 如果对非0的整数（int 包含正数我负数）进行bool类型的转换，那么就全都是True
# a = 1
# print(type(a))
# # 将整数变成布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))

# a = 2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = -1
# print(type(a))
#
# b = bool(a)
# print(b)
# print(type(b))

# a = 0
# print(type(a))
# # 在整数的范围内 0强制类型转换为bool类型的结果是false
# b = bool(a)
# print(b)
# print(type(b))

# 浮点数
# 将浮点数转换为bool类型的数据的时候 正热浮点数和负的浮点数的结果是true
# 如果是0.0，那么结果是false
# a = -1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#
# a = 0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字符串
# a = '网红截聊天的图片'
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = '      '
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = ''
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = ""
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候，就返回true
# a = ['关云长','张翼德','赵子龙','马孟起','黄汉升']
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = []
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 元组
# 只要元组中有数据，那么强制类型转换为bool的时候，就会返回true
# a = ('李逵','林冲','卢俊义','武松','李师师')
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 如果元组中没有数据的话，那么就返回False
# a = ()
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#

# 字典
# a = {'name':'武大郎'}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 如果在字典中没有数据的话，那么返回的就是false
# a = {}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 什么情况下是False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))

print(bool(()))
print(bool({}))