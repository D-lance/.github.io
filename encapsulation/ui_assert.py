from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import yaml

f = open(os.path.abspath('./config/element_data.yml'), encoding='utf-8')

element_data = yaml.load(f)


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self, locator):
        """
        定位到元素，
        返回元素对象，
        没定位到，
        Timeout异常
        """
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele

    def findElements(self, locator):
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except Exception:
            return []

    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        """
        判断元素是否被选中，
        返回bool值
        """
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s" % n)
            return True

    def is_title(self, _title):
        """
        返回bool值

        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value):
        """返回bool值, value为空字符串，返回Fasle"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)

    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")

    zentao.sendKeys(loc1, "root")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)
