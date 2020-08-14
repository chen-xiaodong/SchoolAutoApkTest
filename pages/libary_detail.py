"""

@FileName: libary_detail.py
@Author: chenxiaodong
@CreatTime: 2020/8/10 15:44
@Descriptions: 

"""
from pages.base_page import BasePage


class LibraryDetail(BasePage):

    @property
    def calendar(self):
        """
        :@param:
        :@return:

        """
        return self.find_id('lib_build_award_get_parent1')
