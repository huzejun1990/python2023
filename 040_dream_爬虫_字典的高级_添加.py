# @Author : huzejun
# @Time : 2023/1/13 18:03

person = {'name':'老马'}

print(person)

# 给字典添加一个新的key value
# 如果使用变量名字['键'] = 数据时 这个键如果在字典中不存在 那么就会变成新增元素
person['age'] = 18

# 如果这个键在字典中存在 那么就会变成修改元素
person['name'] = '老王'

print(person)