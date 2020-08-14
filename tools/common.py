"""

@FileName: common.py
@Author: chenxiaodong
@CreatTime: 2020/8/12 13:51
@Descriptions: 

"""
import multiprocessing
import os
from threading import Thread
from time import sleep

import requests

from tools import config
from tools.DriverFactory import Driver
from tools.adb import adb as adb_shell


def get_response(method, url, data=""):
    """
    :@param:
    :@return:

    """
    if method == "get":
        r = requests.get(url)
        return r.json()
    elif method == "post":
        r = requests.post(url, data=data)
        return r.json()
    else:
        return "The requests method not support,please change your method"


def start_appium_server(adb):
    print("appium start")
    # os.system("appium")
    adb.start_appium()
    return


def start_driver(desired_caps):
    print("driver start")
    drivers = Driver(desired_caps)
    driver = drivers.start_driver()
    # queues.put(driver)
    driver.implicitly_wait(3)
    # driver.find_element_by_android_uiautomator()
    return driver


def test_thread():
    print("thread1")


def test_thread2():
    print('thread2')


def before_test():
    # print("come in ")
    device = config.get_adb_devices()
    adb = adb_shell(device)
    adb.connect()
    print("adb connect success")
    print("starting appium")
    driver = start_driver(config.get_desired_caps())
    # thread1 = Thread(target=start_appium_server(adb))
    # thread2 = Thread(target=start_driver(config.get_desired_caps(), queues))
    # thread1.setDaemon(True)
    # thread1.start()
    # thread1.join()
    # sleep(20)
    # thread2.start()
    return driver
