from appium import webdriver
from selenium.webdriver import ActionChains

from tools import config, DriverFactory

#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', config.get_desired_caps())
# schools = driver.find_elements_by_id('tv_menu_title')
# print(schools)
# # action = ActionChains(driver)
# # action.move_to_element(schools[3])
# schools[4]
# driver.find_element_by_accessibility_id()
# driver.keyevent(22)
# driver.keyevent(22)
# driver.keyevent(22)
# driver.keyevent(20)
# driver.keyevent(20)
# driver.keyevent()
from tools.DriverFactory import Driver
from tools.adb import adb

# get device
device = config.get_adb_devices()
# get desired_caps
desired_caps = config.get_desired_caps()
# adb init
adb = adb(device)
# adb connect
adb.connect()
# adb start appium
adb.start_appium()
# start driver
driver = Driver(desired_caps)
driver.start_driver()