# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，
# list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。
# 可以添加ids参数指定用例说明(别名)
import pytest
import yaml

# def add_fun(a, b):
#     return a + b + 10
# @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yml"))["datas"],
#                          ids=yaml.safe_load(open("data.yml"))["myids"])
# def test_add(a, b, expected):
#     assert add_fun(a, b) == expected

# def get_datas():
#     with open("data.yml") as f:
#         datas = yaml.safe_load(f)
#         print(datas)   # {'datas': [[1, 1, 12], [-1, -2, 7], [1000, 1000, 2010]], 'myids': ['one', 'two', 'three']}
#         print(50 * '*')
#         # 获取文件中key为datas的数据
#         add_datas = datas["datas"]
#         print(50 * '-')
#         print(add_datas)   #[[1, 1, 12], [-1, -2, 7], [1000, 1000, 2010]]
#         # 获取文件中key为myids的数据
#         add_ids = datas["myids"]
#         print(50 * '+')
#         print(add_ids)   #['one', 'two', 'three']
#         return [add_datas, add_ids]
#
# def add_fun(a, b):
#     return a + b + 10
# @pytest.mark.parametrize("a, b, expected", get_datas()[0], ids=get_datas()[1])
# def test_add(a, b, expected):
#     assert add_fun(a, b) == expected


