# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
# class TestMru():
#     def setup_method(self, method):
#         self.driver = webdriver.Chrome()
#         self.vars = {}
#
#     def teardown_method(self, method):
#         self.driver.quit()
#
#     def wait_for_window(self, timeout=2):
#         self.driver.delete_all_cookies()
#         time.sleep(round(timeout / 1000))
#         wh_now = self.driver.window_handles
#         wh_then = self.vars["window_handles"]
#         if len(wh_now) > len(wh_then):
#             return set(wh_now).difference(set(wh_then)).pop()
#
#     def test_mru(self):
#         self.driver.get("https://mr4u.mymru.ca/")
#         self.driver.set_window_size(1506, 927)
#         self.driver.find_element(By.CSS_SELECTOR, ".Active > .Active").click()
#         time.sleep(3)
#         self.vars["window_handles"] = self.driver.window_handles
#         self.driver.find_element(By.CSS_SELECTOR, ".Left-Navigation > li:nth-child(2) > a").click()
#         time.sleep(3)
#         self.vars["win5792"] = self.wait_for_window(2000)
#         self.vars["root"] = self.driver.current_window_handle
#         self.driver.switch_to.window(self.vars["win5792"])
#         self.driver.find_element(By.LINK_TEXT, "Agent application form").click()
#
#         self.driver.find_element(By.CSS_SELECTOR, ".Qr7Oae:nth-child(2) .whsOnd").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".Qr7Oae:nth-child(2) .whsOnd").send_keys("none")
#         self.driver.find_element(By.CSS_SELECTOR, ".Qr7Oae:nth-child(3) .whsOnd").click()
#         self.driver.close()
#         self.driver.switch_to.window(self.vars["root"])
#         self.driver.close()
