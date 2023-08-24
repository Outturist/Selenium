from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.XPATH,
                                            '//input[@class="form-control first"][@placeholder="Input your first name"]')
    first_name_input.send_keys('Firs Name')

    last_name_input = browser.find_element(By.XPATH,
                                           '//input[@class="form-control second"][@placeholder="Input your last name"]')
    last_name_input.send_keys('Last Name')

    email_input = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
    email_input.send_keys('email')

    phone_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
    phone_input.send_keys('phone')

    address_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
    address_input.send_keys('Address')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


class TestRegistration2(unittest.TestCase):
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.XPATH,
                                            '//input[@class="form-control first"][@placeholder="Input your first name"]')
    first_name_input.send_keys('Firs Name')

    last_name_input = browser.find_element(By.XPATH,
                                           '//input[@class="form-control second"][@placeholder="Input your last name"]')
    last_name_input.send_keys('Last Name')

    email_input = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
    email_input.send_keys('email')

    phone_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
    phone_input.send_keys('phone')

    address_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
    address_input.send_keys('Address')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
