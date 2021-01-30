# coding=utf-8

import pytest
import yaml

# 在导入包之前导入包的路径
import sys

sys.path.append('..')

from pythoncode.calculator import Calculator


# 定义一个读取yml文件的函数，返回yml文件中数组
def get_datas():
    with open(r"D:\pycharm\huogewozi\ck1317\testing\data\cal.yml") as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],
                datas['subt']['datas'],
                datas['mult']['datas'],
                datas['div']['datas'], datas['div1']['datas'])


class TestCator:
    datas: list = get_datas()

    # 测试类的前置条件
    def setup_class(self):
        print(f"测试类前置条件：{'开始计算'}")

    # 测试类的后置条件
    def teardown_class(self):
        print(f"测试类的后置条件：{'开算结束'}")

    # 测试方法的前置条件
    def setup(self):
        print(f"测试方法的前置条件：{'开始计算'}")
        # 实例化一个类
        self.calc = Calculator()

    # 测试方法的后置条件
    def teardown(self):
        print(f"测试方法的后置条件：{'计算结束'}")

    # 参数化加法测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[0])
    def test_add(self, a, b, except_result):
        result = self.calc.add(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化减法测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[1])
    def test_subt(self, a, b, except_result):
        result = self.calc.subt(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化乘法测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[2])
    def test_mult(self, a, b, except_result):
        result = self.calc.mult(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数不为零的测试用例
    @pytest.mark.parametrize('a, b, except_result', datas[3])
    def test_div(self, a, b, except_result):
        result = self.calc.div(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数为零的测试用例
    @pytest.mark.parametrize('a, b, except_result', datas[4])
    def test_div1(self, a, b, except_result):
        with pytest.raises(ZeroDivisionError) as e:
            self.calc.div(a, b)
        print(f"a={a},b={b},except_result={except_result},e.value={e.value}")
        assert except_result in str(e.value)


if __name__ == '__main__':
    pytest.main()
