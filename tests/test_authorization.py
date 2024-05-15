import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password, valid_phone, valid_ls, valid_login


@pytest.fixture(autouse=True)
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(10) #Неявные ожидания
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/')

    yield driver

    driver.quit()

####################### ПО НОМЕРУ ТЕЛЕФОНА

def test_auth_positive_valid_tel_and_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь успешно авторизируется по корректному номеру телефона
     и корректному паролю, и перейдет на страницу своего личного кабинета'''
    # Выбираем вкладку "Телефон"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что мы оказались в личном кабинете пользователя
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]').text == "Учетные данные"



def test_auth_negative_invalid_tel_and_valid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
    номеру телефона и корректному паролю'''
    # Выбираем вкладку "Телефон"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys("+71234567890")
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"


def test_auth_negative_valid_tel_and_invalid_pass(driver):
    '''Этот тест проверяет, что пользователь не сможет успешно авторизоваться по корректному номеру телефона и
    некорректному паролю'''
    # Выбираем вкладку "Телефон"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_invalid_tel_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
     номеру телефона и некорректному паролю'''
    # Выбираем вкладку "Телефон"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('+71234567890')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

####################### ПО ЭЛЕКТРОННОЙ ПОЧТЕ


def test_auth_positive_valid_mail_and_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь успешно авторизируется по корректной почте и
    корректному паролю, и перейдет на страницу своего личного кабинета'''
    # Выбираем вкладку "Почта"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что мы оказались в личном кабинете пользователя
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]').text == "Учетные данные"

def test_auth_negative_invalid_mail_and_valid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректной почте
     и корректному паролю'''
    # Выбираем вкладку "Почта"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('invalid_email@mail.ru')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_valid_mail_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по корректной почте
     и некорректному паролю'''
    # Выбираем вкладку "Почта"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_invalid_mail_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректной почте
     и некорректному паролю'''
    # Выбираем вкладку "Почта"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('invalid_email@mail.ru')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"


####################### ПО ЛОГИНУ



def test_auth_positive_valid_login_and_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь успешно авторизируется по корректному логину и
    корректному паролю, и перейдет на страницу своего личного кабинета'''
    # Выбираем вкладку "Логин"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим логин пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что мы оказались в личном кабинете пользователя
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]').text == "Учетные данные"

def test_auth_negative_invalid_login_and_valid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
    логину и корректному паролю'''
    # Выбираем вкладку "Логин"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим логин пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('invalid_login')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_valid_login_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по корректному логину
     и некорректному паролю'''
    # Выбираем вкладку "Логин"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим логин пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_invalid_login_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
    логину и некорректному паролю'''
    # Выбираем вкладку "Логин"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим логин пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('invalid_login')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

####################### ПО ЛИЦЕВОМУ СЧЕТУ


def test_auth_positive_valid_ls_and_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь успешно авторизируется по корректному лицевому счету и
    корректному паролю, и перейдет на страницу своего личного кабинета'''
    # Выбираем вкладку "Лицевой счет"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим лицевой счет пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что мы оказались в личном кабинете пользователя
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]').text == "Учетные данные"

def test_auth_negative_invalid_ls_and_valid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
    лицевому счету и корректному паролю'''
    # Выбираем вкладку "Лицевой счет"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим лицевой счет пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('123456789012')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_valid_ls_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по корректному
    лицевому счету и не корректному паролю'''
    # Выбираем вкладку "Лицевой счет"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим лицевой счет пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_auth_negative_invalid_ls_and_invalid_pass(driver):
    '''Этот тест проверяет, что зарегистрированный пользователь не сможет успешно авторизоваться по некорректному
    лицевому счету и не корректному паролю'''
    # Выбираем вкладку "Лицевой счет"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим лицевой счет пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys('123456789012')
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys('invalid_password')
    # Вводим капчу
    time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что пользователь ввел не корректные данные и не может перейти в личный кабинет
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

