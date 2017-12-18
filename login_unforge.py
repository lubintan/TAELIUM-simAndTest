# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, sys

URL = None
PASSWORD = None


class Login_unforge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = URL
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_alpha3_login_forge(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(10)
        try:
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            # print "click returning user"
            time.sleep(1)
        finally:
            driver.find_element_by_css_selector("i.fa.fa-key").click()
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys(PASSWORD)
        driver.find_element_by_xpath("//button[@onclick=\"NRS.login(1,$('#login_password').val())\"]").click()
        driver.find_element_by_xpath("//button[@onclick=\"NRS.login(1,$('#login_password').val())\"]").click()

        time.sleep(3)
        driver.find_element_by_css_selector("#forging_indicator > i.fa.fa-circle").click()
        time.sleep(3)
        driver.find_element_by_id("stop_forging_password").send_keys(PASSWORD)
        driver.find_element_by_id("stop_forging_button").click()

        # time.sleep(10)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def run():
    unittest.main()

if __name__ == "__main__":
    # URL = "http://54.255.130.192:43250/"
    # PASSWORD = "password4"

    allInput = raw_input()
    inputArray = allInput.split(",")
    URL = inputArray[0]
    PASSWORD = inputArray[1]

    unittest.main()
