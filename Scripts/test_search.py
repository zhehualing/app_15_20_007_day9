from Base.page import Page
from Base.driver import Driver
from Base.analysysData import AnalysisData
import pytest, yaml, os


# 解析数据方法 -先在data临时见一个py文件 方便解析数据
def get_data():
    # 存储测试数据
    data_list = []
    # 获取yaml文件数据
    data = AnalysisData.get_yaml_data("search.yml")
    for i in data.values():
        data_list.append((i.get("input"), i.get("exp")))
    return data_list


class TestSearch:

    def setup_class(self):
        """点击搜索按钮"""
        Page.get_setting().click_search_btn()

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.mark.parametrize("search_text, search_exp", get_data())
    def test_search(self, search_text, search_exp):
        """
        搜索内容测试
        :param search_text: 搜索内容
        :param search_exp: 搜索预期结果
        :return:
        """
        # 搜索
        result = Page.get_search().get_search_result(search_text)
        # 断言
        assert search_exp in result
