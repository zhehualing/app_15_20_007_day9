"""这个driver可以完成多平台声明"""
from appium import webdriver


class Driver:
    # app的driver变量声明
    app_driver = None

    # 声明手机driver
    @classmethod  # 不实例化类 也可以调用方法
    def get_app_driver(cls):
        """声明手机驱动对象"""
        if not cls.app_driver:
            # app_driver为None时候，没有对象 需要声明
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明手机驱动对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver
        else:
            # app_driver是有对象 没必要在声明一次
            return cls.app_driver

    # 退出手机driver
    @classmethod
    def quit_app_driver(cls):
        """退出手机驱动对象"""
        if cls.app_driver:
            # app_driver有对象
            # 退出driver
            cls.app_driver.quit()
            # 初始化app_driver为None
            cls.app_driver = None
