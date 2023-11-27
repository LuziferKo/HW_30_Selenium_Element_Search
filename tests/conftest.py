import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


@pytest.fixture(autouse=True)
def testing():
    cService = webdriver.ChromeService(executable_path='C:/Users/User/Downloads/chromedriver/chromedriver.exe')
    pytest.driver = webdriver.Chrome(service=cService)

    pytest.driver.set_window_size(1400, 1000)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


@pytest.fixture()
def test_show_my_pets():
    """Авторизация на сайте и переход на страницу Мои питомцы"""
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Проверка, что сайт открыт на странице "Мои питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
