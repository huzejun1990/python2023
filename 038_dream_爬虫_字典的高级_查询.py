# @Author : huzejun
# @Time : 2023/1/13 17:42

# 定义一个字典
person = {'name':'张三','age':28}

# 访问person的name
# print(person['name'])
# print(person['age'])

# 使用中[]的方式 获取字典中不存在的key的时候 会发生异常 KeyError
# print(person['sex'])

# 不能使用.的方法来访问字典的数据
# print(person.name)

# print(person.get('name'))
# print(person.get('age'))

# 使用.的方式，获取字典中不存在的key的时候 会返回 None值
print(person.get('sex'))