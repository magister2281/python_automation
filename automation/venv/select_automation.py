from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_num = browser.find_element_by_css_selector('span[id="num1"]')
    second_num = browser.find_element_by_css_selector('span[id="num2"]')
    fir = int(first_num.text)
    sec = int(second_num.text)
    result = fir + sec
    select = Select(browser.find_element_by_css_selector('select[class="custom-select"]'))
    select.select_by_visible_text(str(result))
    submit_but = browser.find_element_by_css_selector('button[type="submit"]')
    submit_but.click()
finally:
    time.sleep(10)
    browser.quit()