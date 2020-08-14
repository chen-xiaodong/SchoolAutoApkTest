"""

@FileName: adb.py
@Author: chenxiaodong
@CreatTime: 2020/8/6 15:54
@Descriptions: 

"""
import os
import subprocess
from time import sleep


class adb:
    def __init__(self, device):
        self.device = device

    def connect(self):
        self.disconnect()
        self.adb_kill()
        p = subprocess.run("adb connect " + self.device, shell=True, stdout=subprocess.PIPE)
        if "failed" not in p.stdout.decode("GBK"):
            p2 = subprocess.run("adb devices", shell=True, stdout=subprocess.PIPE)
            if p2.returncode == 0:
                connected_device = p2.stdout.decode("GBK").split('\n')[1].split('\t')[0]
                if connected_device == self.device:
                    return 1
                else:
                    if self.retry() == 0:
                        return 1
            else:
                if self.retry() == 0:
                    return 1
        else:
            if self.retry() == 0:
                return 1

    def retry(self):
        while 1:
            sleep(5)
            print("waiting for adb connect")
            if self.connect() == 1:
                break
        return 0

    def disconnect(self):
        p = subprocess.run(["adb disconnect " + self.device], shell=True)
        if p.returncode == 0:
            return

    def adb_kill(self):
        """
        :@param:
        :@return:

        """
        subprocess.run("adb kill-server", shell=True)

    def install(self):
        pass

    def uninstall(self):
        pass

    def start_appium(self):

        """
        :@param:
        :@return:
        """
        cmd = "appium"
        subprocess.Popen(cmd, shell=True)
        sleep(20)

    def close_appium(self):
        pass
