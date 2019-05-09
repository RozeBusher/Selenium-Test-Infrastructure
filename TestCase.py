import time
import unittest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

#C:\Program Files\Firefox\firefox.exe
#E:\APP Pack\\Network\Firefox\geckodriver.exe

#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
#E:\APP Pack\Network\Chrome\chromedriver.exe

class BaiduTest(unittest.TestCase):
    url="https://www.baidu.com"
    fstr = "C:\\Program Files\\Firefox\\firefox.exe"
    fgstr="E:\\APP Pack\\Network\\Firefox\\geckodriver.exe"
    cstr="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    cgstr="E:\\APP Pack\\Network\\Chrome\\chromedriver.exe"
    lckw=(By.ID, 'kw')
    lcsu=(By.ID, 'su')
    lcrst=(By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver=webdriver.Firefox(firefox_binary=self.fstr, executable_path=self.fgstr)
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.find_element(*self.lckw).send_keys("弱智吧")
        self.driver.find_element(*self.lcsu).click()
        time.sleep(5)
        rst=self.driver.find_elements(*self.lcrst)
        for a in rst:
            print(a)

    def test_2(self):
        self.driver.find_element(*self.lckw).send_keys("Starcraft II"+Keys.RETURN)
        time.sleep(5)
        rst=self.driver.find_elements(*self.lcrst)
        for a in rst:
            print(a)

class CPTest(unittest.TestCase):

    def algo(self, N):
        N = str(N)
        if len(N) > 4:
            n = N[len(N) - 5:len(N)]
        else:
            n = N
        n = int(n)
        n = n % 500
        x = (2019 ** n) % 10000
        return x

    def Setup(self):
        return

    def tearDown(self):
        return

    def test_1(self):
        t=self.algo(2)
        assert(t==6361)

    def test_2(self):
        t=self.algo(4)
        assert(t==2321)

    def test_3(self):
        t=self.algo(1067)
        assert(t==939)