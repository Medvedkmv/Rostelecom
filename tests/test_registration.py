import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password, valid_phone, valid_ls, valid_login, valid_name, valid_surname



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

def test_registr_negative_duplicate_user(driver):
    '''Этот тест проверяет, что ранее зарегистрированный пользователь не сможет повторно зарегистрироваться
    с использованием тех же данных'''
    # Нажимаем на кнопку "Зарегистрироваться"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим Имя пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(valid_name)
    # Вводим Фамилию пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(valid_surname)
    # Выбираем регион пользователя
    WDW(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')))
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]').click()
    # time.sleep(10)

    # Вводим электронную почту или телефон
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'address')))
    if valid_email != 0:
        driver.find_element(By.ID, 'address').send_keys(valid_email)
    else:
        driver.find_element(By.ID, 'address').send_keys(valid_phone)
    # Вводим пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим подтверждение пароля пароль
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку зарегистрироваться
    WDW(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-btn')))
    driver.find_element(By.CLASS_NAME, 'rt-btn').click()
    # Проверяем, что пользователь не может зарегистрироваться повторно
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/h2[1]').text == "Учётная запись уже существует"


def test_registr_negative_user_name_less_2_sym(driver):
    '''Этот тест проверяет, что новый пользователь не сможет успешно зарегистрируется с использованием некорректного
    имени состоящего из < 2 символов'''
    # Нажимаем на кнопку "Зарегистрироваться"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим Имя пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('А')
    # Вводим Фамилию пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(valid_surname)
   # Проверяем, что имя пользователя некорректное
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



def test_registr_negative_user_name_more_30_sym(driver):
    '''Этот тест проверяет, что новый пользователь не сможет успешно зарегистрируется с использованием некорректного
    имени состоящего из > 30 символов'''
    # Нажимаем на кнопку "Зарегистрироваться"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим Имя пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Абвгдеёжзийклмнопрстуфхцчшщъыьэ')
    # Вводим Фамилию пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(valid_surname)
   # Проверяем, что имя пользователя некорректное
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_registr_negative_user_name_latin_sym(driver):
    '''Этот тест проверяет, что новый пользователь не сможет успешно зарегистрируется с использованием некорректного
     имени латинскими буквами'''
    # Нажимаем на кнопку "Зарегистрироваться"
    WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим Имя пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Brad')
    # Вводим Фамилию пользователя
    WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')))
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(valid_surname)
   # Проверяем, что имя пользователя некорректное
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."







