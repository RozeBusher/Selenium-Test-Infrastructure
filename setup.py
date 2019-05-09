#
# import time
#
# fstr="C:\\Program Files\\Firefox\\firefox.exe"
# fgstr="E:\\APP Pack\\Network\\Firefox\\geckodriver.exe"
#
# cstr="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# cgstr="E:\\APP Pack\\Network\\Chrome\\chromedriver.exe"
#
#
# driver=webdriver.Chrome(cgstr)
# driver.get('i.qq.com')
#
# driver=webdriver.Firefox(firefox_binary=fstr, executable_path=fgstr)
# #driver.get("https://google.com")
# #driver.execute_script('''window.open("http://baidu.com", "_blank");''')
# driver.get("https://baidu.com")
# driver.find_element_by_id("kw").send_keys("ruozhiba"+Keys.RETURN)
# driver.execute_script('''window.open()''')
# print(driver.window_handles)
# print(driver.current_window_handle)
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://google.com")
# print(driver.window_handles)
# print(driver.current_window_handle)
# driver.find_element_by_name("q").send_keys("弱智吧"+Keys.RETURN)

#Appium


#unittest infrastructure
# import unittest
# import TestCase
#
# if __name__=='__main__':
#     suite=unittest.TestLoader().loadTestsFromTestCase(TestCase.CPTest)
#     unittest.TextTestRunner(verbosity=2).run(suite)


