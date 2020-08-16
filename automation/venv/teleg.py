from selenium import webdriver
import time
import os
link = "https://web.telegram.org/#/login"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(60)
    browser.get('')
    while True:
        browser.get('')
        send_1 = browser.find_element_by_css_selector('div[class="composer_rich_textarea"]').send_keys("привет")
        send_2 = browser.find_element_by_css_selector('span[class="im_submit_send_label nocopy"]').click()



finally:
   pass