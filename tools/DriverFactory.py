"""

@FileName: DriverFactory.py
@Author: chenxiaodong
@CreatTime: 2020/8/8 12:46
@Descriptions: 

"""
from appium import webdriver


class Driver:
    def __init__(self, desired_caps):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def start_driver(self):
        # self.close_driver()
        return self.driver

    def close_driver(self):
        self.driver.close()
