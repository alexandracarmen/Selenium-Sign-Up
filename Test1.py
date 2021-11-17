from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest

chrome_options = Options()
chrome_options.add_argument("[path to the profile]")
driver = webdriver.Chrome(r"C:\Users\Alexandra\PycharmProjects\TestSelenium\Drivers\chromedriver.exe")
driver.get("https://politrip.com/account/sign-up")

class MySignUp(unittest.TestCase):

    def setUp(self):
        self.drive=webdrive.Chrome()
    def test_sign_up(self):
        driver = self.driver
        driver.get('https://politrip.com/account/sign-up')
        time.sleep(3)

        driver.find_element_by_css_selector('first-text')
        time.sleep(3)
        fname = driver.find_element_by_id('first-name')
        fname.clear()
        time.sleep(3)
        fname.send_keys('Alexandra')
        lname= driver.find_element_by_id('last-name')
        lname.clear()
        time.sleep(3)
        lname.send_keys('Sescu')
        email=driver.find_element_by_id('email')
        email.clear()
        time.sleep(3)
        email.send_keys('alexandracarmen187487@yahoo.com')
        pwd = driver.find_element_by_id('sign-up-password-input')
        pwd.clear()
        time.sleep(3)
        pwd.send_keys('Adaytoremember896')
        pwdconfirm = driver.find_element_by_id('sign-up-confirm-password-input')
        pwdconfirm.clear()
        time.sleep(3)
        pwdconfirm.send_keys('Adaytoremember896')
        heard = driver.find_element_by_id('sign-up-heard-input')
        heard.clear()
        time.sleep(3)
        heard.send_keys('Other')
        driver.find_element_by_id('qa_loader-button').click()
        time.sleep(100)
        participant =driver.find_element_by_id('qa_signup-participant').click()
        participant.clear()
        time.sleep(3)
        cur_url = driver.current_url
        expected_url = 'https://politrip.com/'
        try:
            self.assertEqual(cur_url, expected_url, "Expected ursl not")
        except Exception as ex:
            print(ex)

    if __name__ != "main.py":
        pass
    else:
        unittest.main()
