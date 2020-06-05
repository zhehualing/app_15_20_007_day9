from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self):
        super().__init__()

    def get_search_result(self, text):
        """
        输入搜索内容 获取搜索结果
        :param text: 搜索内容
        :return: 搜索结果文本列表
        """
        # 输入
        self.send_ele(PageElements.search_input, text)
        # 获取搜索结果
        results = self.search_eles(PageElements.search_result)
        # 返回搜索结果文本列表[,,]
        return [i.text for i in results]
