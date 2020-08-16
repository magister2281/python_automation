from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('div[class="first_block"] input[class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('div[class="first_block"] input[class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('div[class="first_block"] input[class="form-control third"]')
    input3.send_keys("test@gmail.com")
    input4 = browser.find_element_by_css_selector('div[class="second_block"] input[class="form-control first"]')
    input4.send_keys("Russia")
    input4 = browser.find_element_by_css_selector('div[class="second_block"] input[class="form-control second"]')
    input4.send_keys("Russia")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
