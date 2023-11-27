import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_have_complete_info(test_show_my_pets):
    """Проверка, что на странице 'Мои питомцы' у всех питомцев есть имя, возраст и порода"""
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table.table-hover tbody tr')))

    pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    for i in range(len(pet_info)):
        data = pet_info[i].text.replace('\n', '').replace('*', '')
        split_data = data.split(' ')
        result = len(split_data)
        assert result == 3