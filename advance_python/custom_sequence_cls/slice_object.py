"""
实现可切片的对象：
    根据序列协议实现该实现的魔法函数（看abc源码）
"""
import numbers
class Group:
    """
    支持切片操作
    """
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

if __name__ == '__main__':
    staffs = ['yinlei', 'zengziyuan', 'zhangwuli', 'dufengqiang', 'yinjianyun', 'hushanghui', 'xiabo', 'tangyuzhang', 'liuhanchang']
    group = Group(company_name='china unicom', group_name='fucheng', staffs=staffs)
    sub_group = group[:2]
    print(sub_group)
    print(group[0])
    if "yinlei" in group:
        print('yinlei is contained china unicom')
    reversed(group)
    for item in group:
        print(item)