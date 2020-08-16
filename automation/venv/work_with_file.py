from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Алекс')
    second_name = browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Армандун')
    email = browser.find_element_by_css_selector('input[name="email"]').send_keys('test@gmail.com')
    element = browser.find_element_by_css_selector('input[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    create_file = open("file.txt",'w')
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    submit = browser.find_element_by_css_selector('button[class="btn btn-primary"]').click()

finally:
    time.sleep(5)
    browser.quit()
