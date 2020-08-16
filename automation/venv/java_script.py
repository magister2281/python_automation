from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return math.log(abs(12*math.sin(x)))
    first = browser.find_element_by_css_selector('span[id="input_value"]')
    x = int(first.text)
    result = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element_by_css_selector('input[id="answer"]').send_keys(str(result))
    robot = browser.find_element_by_css_selector('input[class="form-check-input"]')
    robot.click()
    switch = browser.find_element_by_css_selector('input[id="robotsRule"]')
    switch.click()
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()