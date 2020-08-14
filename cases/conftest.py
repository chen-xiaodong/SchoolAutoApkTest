"""

@FileName: conftest.py
@Author: chenxiaodong
@CreatTime: 2020/8/12 15:13
@Descriptions: 

"""
import pytest
from threading import Thread
from pages import index_page
from tools import config, common
from tools.DriverFactory import Driver
from tools.adb import adb as adb_shell


def start_appium_server(adb, device):
    print("appium start")
    adb.start_appium()


def opt_driver(desired_caps,opt="close"):
    print("driver start")
    drivers = Driver(desired_caps)
    if opt =="start":
        driver = drivers.start_driver()
    else:
        driver.close_driver


@pytest.fixture()
def start():
    print("come in ")
    device = config.get_adb_devices()
    adb = adb_shell(device)
    adb.connect()
    threads = []
    thread1 = Thread(target=start_appium_server(adb, device))
    thread1.setDaemon(True)
    thread1.start()
    yield
    opt_driver(config.get_desired_caps())




