# @Author : huzejun
# @Time : 2023/1/13 18:18

# del
#   （1） 删除字典中指定的某一个元素
person = {'name':'老马','age':18}
#
# # 删除之前
# print(person)
#
# del person['age']
#
# # 删除之后
# print(person)


# (2) 删除整个字典
# 删除之前
# print(person)
#
# del person
#
# # 删除之后
# print(person)

# clear
# (3) 清空字典 但是保留字典对象
print(person)

person.clear()

print(person)
