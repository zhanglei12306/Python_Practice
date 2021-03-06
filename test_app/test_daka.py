import os
import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class TestCase:
    def setup(self):
        # server 启动参数
        desired_caps = {}

        # 设备信息
        # 平台的名称
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '6.0.1'
        # 设备号
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 启动的包
        desired_caps['appPackage'] = 'com.tencent.wework'
        # 启动的Activity
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # 键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['settings[waitForIdleTimeout'] = 0

        # 只有声明驱动对象我们才可以让手机完成脚本的操作,声明的方法如下:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明对象后会直接启动参数中的应用
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq'  and  @text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        daka = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/pt").text
        assert daka == '外出打卡成功'












