import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_half_pets_have_photo(test_show_my_pets):
    """Проверка того, что хотя бы у половины питомцев на странице 'Мои питомцы' есть фото"""
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    user_statistic = pytest.driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    number = user_statistic.text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    half = number // 2

    # Поиск количества питомцев с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1

    # Проверка того, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_of_photos >= half
