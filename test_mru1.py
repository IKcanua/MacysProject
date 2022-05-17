import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestMru1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.vars = {}

    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_mru1(self):
        self.driver.get("https://mr4u.mymru.ca/")
        self.driver.set_window_size(1900, 1000)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div/li/a[@title="Request information"]').click()
        self.driver.find_element(By.ID, "ToggleLink1").click()
        self.driver.find_element(By.NAME, "firstName").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("Machael")
        self.driver.find_element(By.NAME, "preferredFirstName").click()
        self.driver.find_element(By.NAME, "preferredFirstName").send_keys("Mikkjlk")
        self.driver.find_element(By.NAME, "lastName").click()
        self.driver.find_element(By.NAME, "lastName").send_keys("gfhsfgh")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("fghsf")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.close()
