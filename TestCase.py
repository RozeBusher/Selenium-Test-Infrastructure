import time
import unittest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import random

#C:\Program Files\Firefox\firefox.exe
#E:\APP Pack\\Network\Firefox\geckodriver.exe

#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
#E:\APP Pack\Network\Chrome\chromedriver.exe

def silent_assert(func, *args, **kwd):
    try:
        #print(*args)
        #print(**kwd)
        func(*args, **kwd)
    except Exception as e:
        print(e)

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
        #self.driver.quit()
        return

    def test_1_Gen(self):
        self.driver.find_element(*self.lckw).send_keys("弱智吧")
        self.driver.find_element(*self.lcsu).click()
        time.sleep(5)
        rst=self.driver.find_elements(*self.lcrst)
        ele=rst[0]
        act=ActionChains(self.driver)
        act.move_to_element(ele)
        act.click()
        act.perform()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        turl=self.driver.current_url
        turl=turl+"/f?kw=%E5%BC%B1%E6%99%BA&ie=utf-8&tab=good"
        js="\'\'\'window.open(\""+turl+"\", \"_blank\");\'\'\'"
        print(turl)
        print(js)
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(*self.lckw).clear()

    @unittest.skip("SKIP FOR NOW")
    def test_2_SC2(self):
        self.driver.find_element(*self.lckw).send_keys("Starcraft II"+Keys.RETURN)
        time.sleep(5)
        rst=self.driver.find_elements(*self.lcrst)
        for a in rst:
            print(a)

    @unittest.skip("SKIP FOR NOW")
    def test_3_shortcut(self):
        self.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, 't')

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

    def test_3eq(self):
        self.assertEqual(self.algo(1067), 939)

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (3, 2, 1))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

class Semantic(unittest.TestCase):
    a=0

    def setUp(self):
        self.a=self.a+1
        self.skipTest("skip for test")

    def tearDown(self):
        self.a=self.a+1
        return

    @unittest.skip("skip fow now")
    def test_3(self):
        print(self.a)
        return

    def test_2(self):
        print(self.a)
        return

    def test_1(self):
        print(self.a+1)
        return

    def test_4(self):
        with self.assertRaises(ValueError):
            print(int('N/A'))
        return

class SCalc(unittest.TestCase):
    def setUp(self):
        return
        #if(self.plus(-1, 2)!=2):
            #self.skipTest("UNCLEAN")

    def tearDown(self):
        return

    def plus(self, a:int, b:int):
        return a+b

    def minus(self, a:int, b:int):
        return a-b

    def test_1(self):
        self.assertEqual(self.plus(1, 1), 2)
        #silent_assert(self.assertEqual, self.plus(-1, 2), 1000)
        #silent_assert(self.assertEqual, self.plus(2, 2), 5)
        self.assertEqual(self.plus(-1, 2), 2)
        #self.assertEqual(self.plus(-1, 2), 3)

    def test_2(self):
        self.assertEqual(self.minus(2, 1), 1)
        self.assertEqual(self.minus(1, -2), 3)