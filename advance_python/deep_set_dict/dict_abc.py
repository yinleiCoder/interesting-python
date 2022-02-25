"""
dict的abc继承关系：
    dict属于Mapping类型
    class dict(MutableMapping[_KT, _VT], Generic[_KT, _VT]):

"""
from collections.abc import Mapping, MutableMapping

a = {}
print(isinstance(a, MutableMapping))