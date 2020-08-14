"""

@FileName: base_page.py
@Author: chenxiaodong
@CreatTime: 2020/8/8 12:54
@Descriptions: 

"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_id(self, element_id):
        return self.driver.find_element_by_id(element_id)

    def find_access_id(self, element_id):
        return self.driver.find_element_by_accessibility_id(element_id)

    def find_ids(self, elements_id):
        return self.driver.find_elements_by_id(elements_id)

    def find_name(self, element_name):
        return self.driver.find_element_by_name(element_name)

    def find_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def key_down(self):
        return self.driver.keyevent(20)

    def key_right(self):
        return self.driver.keyevent(22)

    def key_left(self):
        return self.driver.keyevent(21)

    def key_up(self):
        return self.driver.keyevent(19)

    def confirm(self):
        return self.driver.keyevent(66)

    def wait(self):
        pass

    def find_by_uiautomation(self, text):
        return self.driver.find_element_by_android_uiautomator(text)

    def deal_opt(self, action):
        """
        :@param:
        :@return:

        """
        if action == 'up':
            self.key_up()
        elif action == 'right':
            self.key_right()
        elif action == 'left':
            self.key_left()
        elif action == 'down':
            self.key_down()
        elif action == 'confirm':
            self.confirm()
        else:
            pass
