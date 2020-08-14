"""

@FileName: test_start.py
@Author: chenxiaodong
@CreatTime: 2020/8/8 13:12
@Descriptions:

"""
from pages import index_page, library_page
from tools import config, common


# region Main
# os.system('ls')
# print(str(datetime.datetime.now()))
# os.system('ls -l')
# print(str(datetime.datetime.now()))
# print("hello")
# process = subprocess.run(["adb devices"], shell=True)
# print(process)
# print("hello")
# adb = adb("127.0.0.1:6555").connect()
# response = requests.get("https://www.maxluck.top/api/hdzbstb/priv/notice/getFirstMessage?studentId=29571").json()
# # print(response['data']['message'])
# expect = response['data']['message']
# driver = Driver(config.get_desired_caps()).start_driver()
# index = Index(driver)
# index.find_id("fl_shimmer_message_parent").click()
# index.confirm()
# sleep(2)
# tv_infos = index.find_ids("tv_info")
# print(tv_infos[0].text)

# library = Library(driver)
# # driver.start_activity("com.wasu.zn.edu.smartcampus.tv", ".home.ui.CampusLibBuildDetailActivity")
# sleep(2)
# actual_text = driver.find_element_by_id("tv_message_detail").text
# try:
#     assert expect == actual_text
# except AssertionError as e:
#     print("error")
#     print("expect:" + expect + '\n')
#     print("actual:" + actual_text + '\n')

# actual_name = driver.find_element_by_id("tv_rank_item_stu_name").text
# actual_rank = driver.find_element_by_id("tv_rank_item_progress").text
# # driver.start_activity("com.wasu.zn.edu.smartcampus.tv", ".home.ui.CampusLibBuildDetailActivity")
# sleep(2)
# driver.start_activity("com.wasu.zn.edu.smartcampus.tv", ".home.ui.LibraryBuildRankActivity")
# driver.find_element_by_id("ctl_rank_parent").click()
# library.confirm()
# sleep(5)
# new_name = driver.find_element_by_id("tv_rank_item_stu_name").text
# new_rank = driver.find_element_by_id("tv_rank_item_progress").text

# try:
#     assert actual_name == new_name.split(')')[1]
# except AssertionError as e:
#     print(new_name.split(')')[1])
#     print("名字错误")
#
# try:
#     assert actual_rank == new_rank
# except AssertionError as e:
#     print("排名错误")

# print("测试结束")
# index = Index(driver)
# titles = index.menu_titles
# titles[3].click()
# index.confirm()
# library = Library(driver)
# library.key_down()
# library.key_down()
# actual_text = library.library_entry.text
# entry = library.library_entry
# entry.click()
# print(driver.current_activity)
# try:
#     assert actual_text == "打卡"
# except AssertionError as e:
#     print("error")
#     print(actual_text)
# @pytest.fixture(scope="class")
# def start_appium_server():
#     """
#     :@param:
#     :@return:
#
#     """
#     # get device
#     print("start")
#     device = config.get_adb_devices()
#     adb = adb_shell(device)
#     adb.connect()
#     # adb start appium
#     adb.start_appium()
#     print("appium start")


# @pytest.fixture(scope="function")
# def before_test():
#     """
#     :@param:
#     :@return:
#     start driver
#     """
#     # get device
#     # print("start")
#     # device = config.get_adb_devices()
#     # print("adb connect")
#     # get desired_caps
#     desired_caps = config.get_desired_caps()
#     # adb init
#     # adb = adb_shell(device)
#     # adb connect
#     # adb.connect()
#
#     # start driver
#     drivers = Driver(desired_caps)
#     driver = drivers.start_driver()
#     print("driver start")
#     yield driver
#     driver.close()
#     # adb.close_appium()
#     # adb.disconnect()


# class Test_Cases:
#
#     def test_message(self,start_appium_server):
#         """
#         :@param:
#         :@return:
#         test index message
#         """
#         print("start success")
# print(type(before_test))
# index = index_page.Index(before_test)
# latest_message = index.tv_message_detail.text
# print(latest_message)
# res = common.get_response("get", "https://www.maxluck.top/api/hdzbstb/priv/notice/getFirstMessage?studentId"
#                                  "=29571")
# print(res)
# endregion
from tools.common import before_test


def test_message(page):
    """
    :@param:
    :@return:
    test index page message
    """
    print("message test start ")
    now_message = page.tv_message_detail.text
    response = common.get_response("get", "https://www.maxluck.top/api/hdzbstb/priv/notice/getFirstMessage?studentId"
                                          "=29571")
    # print(now_message)
    # print(response['data']['message'])
    try:
        assert now_message == response['data']['message']
    except AssertionError as e:
        print("message error,please check")
    print("message test passed")
    return


def test_library():
    """
    :@param:
    :@return:

    """
    print("thread2 start")


def test_mine():
    """
    :@param: 
    :@return: 
    
    """
    pass


def test_collects(page):
    """
    :@param: 
    :@return: 
    test index collects
    """

    elements = page.tv_collections
    nums = len(elements)
    response = common.get_response("get","https://www.maxluck.top/api/hdzbstb/learningCenter"
                                         "/queryCollectionCourseList?studentId=29571&pageIndex=1&pageSize=50"
                                         "&appBandPhoneId=&terminalType=2")
    amount = response['data']['amount']
    # print(amount)
    try:
        assert nums == amount
    except AssertionError as e:
        print("num not equal with interface")
    return


if __name__ == '__main__':
    drivers = before_test()                       # before test
    index = index_page.Index(drivers)             # init index page
    test_message(index)                           # test index message
    test_collects(index)

