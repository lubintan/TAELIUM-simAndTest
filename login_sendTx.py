# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random,sys

URL = None
PASSWORD = None
ACCT = None

class SendTx(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = URL
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_send_tx(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(10)
        try:
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            time.sleep(1)
        finally:
            driver.find_element_by_css_selector("i.fa.fa-key").click()

        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys(PASSWORD)
        driver.find_element_by_xpath("//button[@onclick=\"NRS.login(1,$('#login_password').val())\"]").click()
        driver.find_element_by_xpath("//button[@onclick=\"NRS.login(1,$('#login_password').val())\"]").click()
        self.driver.implicitly_wait(5)
        balanceString = driver.find_element_by_id("account_balance_sidebar").text
        balance = float(balanceString.replace(',', '').split('.')[0])
        print 'balance: ', balance

        amountToSend = round(random.random() * balance)
        if amountToSend < 1:
            amountToSend = 1

        print 'sending: ', amountToSend

        time.sleep(3)
        # sending portion
        driver.find_element_by_css_selector("span.coin-symbol").click()
        driver.find_element_by_id("send_money_recipient").send_keys(ACCT.replace('-',''))
        # driver.find_element_by_id("send_money_amount").clear()
        driver.find_element_by_id("send_money_amount").send_keys(str(amountToSend))
        # driver.find_element_by_id("send_money_fee").clear()
        driver.find_element_by_id("send_money_fee").send_keys("1")
        # driver.find_element_by_id("send_money_password").clear()
        driver.find_element_by_id("send_money_password").send_keys(PASSWORD)

        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
        if amountToSend > 100000:
            driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()

        # time.sleep(10)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def run():
    unittest.main()

if __name__ == "__main__":

    #
    allInput = raw_input()
    inputArray = allInput.split(",")
    URL = inputArray[0]
    PASSWORD = inputArray[1]
    ACCT = inputArray[2]

    # print URL, PASSWORD, ACCT

    unittest.main()
