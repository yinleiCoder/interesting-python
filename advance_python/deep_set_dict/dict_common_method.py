"""
dict的常用方法：

"""
a = {
    'yinlei': {'company': 'chian unicom'},
    'zhangming': {'company': 'master'},
}

# a.clear()

# copy浅拷贝
new_dict = a.copy()
new_dict['yinlei']['company'] = 'master'
print(a)
print(new_dict)

# 深拷贝
import copy
a = {
    'yinlei': {'company': 'chian unicom'},
    'zhangming': {'company': 'master'},
}
new_dict = copy.deepcopy(a)
new_dict['yinlei']['company'] = 'master'
print(a)
print(new_dict)

# fromkeys
new_list = ['yinlei', 'yinwei']
new_dict = dict.fromkeys(new_list, {"company": "master"})
print(new_dict)

# get
print(new_dict.get('yinlei2', {}))

# items
for key, value in new_dict.items():
    print(key, value)

# setdefault
new_dict.setdefault("yinzihao", 6)
print(new_dict)

# update
new_dict.update({'singing': 'brother'})

