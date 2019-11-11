from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPy(TestCase):



    def testCommon(self):

        try:
            def calc(x):
                return str(math.log(math.fabs((12*math.sin(x)))))




            link = "http://suninjuly.github.io/explicit_wait2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            book = browser.find_element_by_id("price")
            book = WebDriverWait (browser, 10).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "100")
            )
            browser.find_element_by_id("book").click()
            number = calc(int(browser.find_element_by_id("input_value").text))
            browser.find_element_by_id("answer").send_keys(number)
            browser.find_element_by_id("solve").click()



        # alert = browser.switch_to.alert
        # alert_text.split(': ')[-1]




        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    # не забываем оставить пустую строку в конце файла
