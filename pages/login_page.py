"""

@FileName: login_page.py
@Author: chenxiaodong
@CreatTime: 2020/8/10 10:45
@Descriptions: 

"""
from pages.base_page import BasePage


class LoginPage(BasePage):

    @property
    def login_with_phone(self):
        """
        :@param:
        :@return:
        login with phone
        """
        return self.find_id("edit_phone")

    @property
    def finish_phone_button(self):
        """
        :@param:
        :@return:
        click finish button
        """
        return self.find_id("tv_finish")

    @property
    def edit_verification_code(self):
        """
        :@param:
        :@return:
        edit verification code
        """
        return self.find_id("edit_verification_code")

    @property
    def finish_code_button(self):
        """
        :@param:
        :@return:

        """
        return self.find_id("fl_finish")
