# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, os
from ethTxHashes import ETH_TX_HASHES

IMG_FILE_PATH = "/Users/Lubin/skynet/preIco/alexisSanchez.jpg"
COUNTRIES = ["Bahrain", "New Zealand", "Malaysia", "Japan", "Thailand"]
TAEL_ADDRESSES = ['TAEL-MVVF-FSWE-4QZF-FXL3B', 'TAEL-VXVQ-APCC-UHDD-7A3ZX', 'TAEL-PGDQ-XR6X-2EAS-9H2KM', 'TAEL-AAAA-BBBB-CCCC-DDDDD']

class ParticipationFormTester(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://taelium.com//wp-login.php"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_participation_form_tester(self):
        ethTxHash = random.choice(ETH_TX_HASHES)
        country = random.choice(COUNTRIES)
        ico_carryover = random.randint(0, 1)
        tael_addr = random.choice(TAEL_ADDRESSES)

        try:
            driver = self.driver
            driver.get(self.base_url)
            driver.find_element_by_id("user_login").clear()
            driver.find_element_by_id("user_login").send_keys("tanlubin")
            driver.find_element_by_id("user_pass").clear()
            driver.find_element_by_id("user_pass").send_keys("BlackbirdFlyAway2018")
            driver.find_element_by_id("rememberme").click()
            driver.find_element_by_id("wp-submit").click()
        except:
            pass

        # driver = self.driver
        driver.get("https://taelium.com/affiliate-area/")
        # time.sleep(3)
        driver.find_element_by_id("tablist1-tab4").click()
        time.sleep(1)
        driver.find_element_by_name("email-201").clear()
        driver.find_element_by_name("email-201").send_keys("taelonehundred@gmail.com")
        driver.find_element_by_name("tel-992").clear()
        driver.find_element_by_name("tel-992").send_keys("1234567890")
        driver.find_element_by_name("EthereumTxHashDescription").clear()
        driver.find_element_by_name("EthereumTxHashDescription").send_keys(ethTxHash)
        driver.find_element_by_name("text-231").clear()
        driver.find_element_by_name("text-231").send_keys(tael_addr)
        # time.sleep(5)
        # driver.find_element_by_name("checkbox-MinETH[]").click()
        # mybox1 = driver.find_element_by_name("checkbox-MinETH[]")
        # time.sleep(2)
        # mybox1.click()





        # if ico_carryover==0:
        #     driver.find_element_by_css_selector("span.wpcf7-list-item.last > input[name=\"checkbox-282\"]").click()
        #


        Select(driver.find_element_by_name("mycountry")).select_by_visible_text(country)
        driver.find_element_by_name("file-890").clear()
        driver.find_element_by_name("file-890").send_keys(IMG_FILE_PATH)
        # time.sleep(2)
        driver.find_element_by_name("file-891").clear()
        driver.find_element_by_name("file-891").send_keys(IMG_FILE_PATH)
        time.sleep(3)

        # driver.find_element_by_name("checkbox-TandCs[]").click()
        # mybox2 = driver.find_element_by_name("checkbox-TandCs[]")
        # time.sleep(2)
        # mybox2.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.find_element_by_css_selector("input.wpcf7-form-control.wpcf7-submit").click()

        time.sleep(8)


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

if __name__ == "__main__":

    while (True):
        try:
            unittest.main()
        except:
            continue
        break
