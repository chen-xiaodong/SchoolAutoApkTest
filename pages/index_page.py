"""

@FileName: index_page.py
@Author: chenxiaodong
@CreatTime: 2020/8/8 12:53
@Descriptions: 

"""
from time import sleep

from pages.base_page import BasePage


class Index(BasePage):

    @property
    def choose_school(self):
        """
        :@param:
        :@return:
        first come in,choose the first school
        """
        return self.find_ids("tv_campus_school_name")

    @property
    def login(self):
        """
        :@param:
        :@return:
        click login
        """
        return self.find_id("ll_member_area")

    @property
    def menu_titles(self):
        """
        :@param:
        :@return:
        menu titles
        """
        return self.find_ids('tv_menu_title')

    @property
    def latest_messages(self):
        """
        :@param:
        :@return:

        """
        return self.find_id("fl_shimmer_message_parent")

    @property
    def tv_message_detail(self):
        """
        :@param:
        :@return:
        index tv message text
        """
        return self.find_id("tv_message_detail")

    @property
    def tv_collections(self):
        """
        :@param:
        :@return:
        tv collections
        """
        opts = ['up', 'right', 'right', 'right', 'right', 'confirm']
        # self.find_id('tv_collection_desc').click()
        sleep(2)
        for opt in opts:
            self.deal_opt(opt)
        return self.find_ids('tv_name')
