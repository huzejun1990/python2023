# @Author : huzejun
# @Time : 2023/1/12 17:05

# append
food_list = ['铁锅炖大鹅','酸菜五花肉']
print(food_list)

food_list.append('小鸡炖蘑菇')
print(food_list)

# insert
char_list = ['a','c','d']
print(char_list)
# index的值就是你想插入数据的那个下标
char_list.insert(1,'b')
print(char_list)

# extend
num_list = [1,2,3]
num1_list = [4,5,6]

num_list.extend(num1_list)
print(num_list)
