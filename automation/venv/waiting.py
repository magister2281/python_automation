from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    if button:
        button2 = browser.find_element_by_css_selector('button[id="book"]').click()
    def calc(x):
        return math.log(abs(12*math.sin(x)))

    first = browser.find_element_by_css_selector('span[id="input_value"]')
    x = int(first.text)
    result = calc(x)
    answer = browser.find_element_by_css_selector('input[id="answer"]').send_keys(str(result))
    submit = browser.find_element_by_css_selector('button[id="solve"]').click()

finally:
    time.sleep(10)
    browser.quit()