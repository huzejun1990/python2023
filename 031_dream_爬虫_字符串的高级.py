# @Author : huzejun
# @Time : 2023/1/12 0:22

# 字符串的常见操作

# 获取长度： len                 len函数可以获取字符串的长度
# 查找内容: find                查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中
# 判断：startswith,endswith     判断字符串是不是以谁谁谁开头/结尾
# 计算出现次数：cout              返回 str 在 start 和 end之间，在mystr里面出现的次数
# 替换内容：replace              替换字符串中指定的内容，如果指定次数count,则替换不会超过count
# 切割字符串：split              通过参数的内容切割字符串
# 修改大小写：upper,lower         将字符串中的大小写互换
# 空格处理：strip                去空格
# 字符串拼接：join                字符串拼接

# 获取长度： len length的缩写 长度
s = 'china'
print(len(s))

s1 = 'china'
print(s1.find('c'))

s2 = 'china'
print(s2.startswith('h'))
print(s2.endswith('n'))

s3 = 'aaabb'
print(s3.count('a'))

s4 = 'cccdd'
print(s4.replace('c', 'd'))

s5 = '1#2#3#4'
print(s5.split('#'))

s6 = 'china'
print(s6.upper())

s7 = 'CHINA'
print(s7.lower())

s8 = '   a   '
print(len(s8))
print(len(s8.strip()))

s9 = 'a'
print(s9.join('hello'))