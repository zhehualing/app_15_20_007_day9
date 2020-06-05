"""管理所有页面元素类"""
from selenium.webdriver.common.by import By


class PageElements:
    """建议：以页面为类 一个页面一个类"""

    """设置页面"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")

    """搜索页面类"""
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")
