from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector('button[class="trollface btn btn-primary"]').click()
    first = browser.window_handles[1]
    browser.switch_to_window(first)
    def calc(x):
        return math.log(abs(12*math.sin(x)))

    first = browser.find_element_by_css_selector('span[id="input_value"]')
    x = int(first.text)
    result = calc(x)
    answer = browser.find_element_by_css_selector('input[id="answer"]').send_keys(str(result))
    submit = browser.find_element_by_css_selector('button[class="btn btn-primary"]').click()

finally:
    time.sleep(30)
    browser.quit()
