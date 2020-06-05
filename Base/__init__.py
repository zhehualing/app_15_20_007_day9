"""Base包 基础操作"""


class Fa:

    def __init__(self):
        self.name = "不一样的烟火～"

    def get_name(self):
        print(self.name)


class So(Fa):

    def __init__(self):
        # super().__init__()
        Fa.__init__(self)

    def use_fa_fun(self):
        """使用父类方法"""
        print("我就是我～")
        # 调用父类
        self.get_name()


So().use_fa_fun()
