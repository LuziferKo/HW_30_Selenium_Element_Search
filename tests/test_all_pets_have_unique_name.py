import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_have_unique_names(test_show_my_pets):
    """Проверка, что у всех питомцев на странице 'Мои питомцы' разные имена"""

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение элементов с информацией о питомцах
    pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Из переменной pet_info перебираются имена, сохраняются имя, порода и возраст.
    # Выбираются имена и добавляются в список 'names'
    names = []
    for i in range(len(pet_info)):
        data = pet_info[i].text.replace('\n', '').replace('*', '')
        split_data = data.split(' ')
        names.append(split_data[0])

    # Перебираются имена, и если имя повторяется, к счётчику 'r' прибавляется единица
    # Если r == 0, значит повторяющихся имён нет
    r = 0
    for i in range(len(names)):
        if names.count(names[i]) > 1:
            r += 1
        assert r == 0
    print(r)
    print(names)
