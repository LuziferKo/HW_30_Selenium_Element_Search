import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_are_present(test_show_my_pets):
    """Проверка, что на странице 'Мои питомцы' присутствуют все питомцы(в соответствии со статистикой пользователя)"""

    # Установка явного ожидания
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение данных статистики пользователя
    user_statistic = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение карточек питомцев
    pet_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Получение количества питомцев на основе данных статистики пользователя
    number = user_statistic.text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получение количества карточек питомцев
    number_of_pets = len(pet_cards)

    # Проверка того, что количество питомцев в статистике пользователя совпадает с количеством карточек питомцев
    assert number == number_of_pets






