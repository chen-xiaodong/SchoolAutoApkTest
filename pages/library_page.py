"""

@FileName: library_page.py
@Author: chenxiaodong
@CreatTime: 2020/8/10 15:05
@Descriptions: 

"""
from pages.base_page import BasePage


class Library(BasePage):
    @property
    def library_entry(self):
        """
        :@param: 
        :@return: 
        
        """
        return self.find_id('tv_to_punch_card')


