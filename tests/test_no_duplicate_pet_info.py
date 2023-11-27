import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_no_duplicate_pet_info(test_show_my_pets):
    """Проверка, что в списке нет питомцев с повторяющейся информацией"""

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираются данные из переменной pet_info
    # сохраняются имя, возраст и порода. Остальное меняется на пустую строку и разделяется пробелом
    list_info = []
    for i in range(len(pet_info)):
        info_pet = pet_info[i].text.replace('\n', '').replace('*', '')
        split_info_pet = info_pet.split(' ')
        list_info.append(split_info_pet)

    # Склеиваются имя, возраст и порода
    # Получившиеся склеенные слова добавляются в строку и между ними вставляется пробел
    line = ''
    for i in list_info:
        line += ''.join(i)
        line += ' '

    # Получение списка из строки line
    list_line = line.split(' ')

    # Превращение списка в множество
    set_list_line = set(list_line)

    # Нахождение колчества элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из колчества элементов списка вычитается количество элементов множества
    result = a - b

    # Если количество элементов == 0, то карточки с одинаковыми данными отсутствуют
    assert result == 0
    print(result)
