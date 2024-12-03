import json
import requests
import allure
from allure_commons.types import Severity
from jsonschema import validate

from resourses import CURRENT_DIR, URL


endpoint = "/users"
text = 'Tired of writing endless social media content? Let Content Caddy generate it for you.'


@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Список пользователей")
@allure.title("Успешный запрос списка пользователей по нескольким параметрам")
def test_users_list():

    """ Проверка на статус код """

    with allure.step("Отправка запроса и проверка на статус код"):
        response = requests.get(URL + endpoint)
        assert response.status_code == 200

    response_json = response.json()

    with allure.step("Проверка значения ключа text"):
        text_value = response_json.get("support", {}).get("text")
        assert text_value == text

    """ Проверка корректной фильтрации по per_page """

    with allure.step("Проверка per_page = 2"):
        response = requests.get(URL + endpoint + '?page=1' + '&per_page=2')
        response_json = response.json()
        assert response_json.get('per_page') == 2

    with allure.step("Проверка per_page = 1"):
        response = requests.get(URL + endpoint + '?page=1' + '&per_page=1')
        response_json = response.json()
        assert response_json.get('per_page') == 1

    with allure.step("Проверка per_page = 7"):
        response = requests.get(URL + endpoint + '?page=1' + '&per_page=7')
        response_json = response.json()
        assert response_json.get('per_page') == 7

    """ Проверка схемы json """

    with allure.step("Валидации схемы json"):
        with open(f'{CURRENT_DIR}/schemas/users_schema.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)