"""

@FileName: config.py
@Author: chenxiaodong
@CreatTime: 2020/8/8 12:13
@Descriptions: 

"""

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': '127.0.0.1:6555',
    'appPackage': 'com.wasu.zn.edu.smartcampus.tv',
    'appActivity': '.home.HomeActivity',
    'noReset': True,  # app will no reset everytime
    'autoGrantPermissions': True,  # app auto get Permissions
    'dontStopAppOnReset': True,  # app will not stop
    # 'automationName': 'UiAutomator1'
}


def get_adb_devices():
    return desired_caps.get("deviceName")


def get_desired_caps():
    """
    :@param:
    :@return:

    """
    return desired_caps
