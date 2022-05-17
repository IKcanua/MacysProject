# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class TestMacys():
#     def setup_method(self):
#         self.driver = webdriver.Chrome()
#         self.vars = {}
#
#     def test_macys(self):
#         self.driver.get("https://www.macys.com/")
#         self.driver.set_window_size(1600, 1000)
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         time.sleep(2)
#         self.driver.find_element(By.ID, "closeButton").click()
#         time.sleep(0.5)
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_118 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_1 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_5991 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_22672 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_26846 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, "#flexid_544 span").click()
#         time.sleep(1)
#         self.driver.delete_all_cookies()
#         self.driver.find_element(By.CSS_SELECTOR, ".fob-red > span").click()
#         self.driver.close()
