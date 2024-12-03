import json
import requests
import allure
from allure_commons.types import Severity
from jsonschema import validate
from resourses import CURRENT_DIR, URL


@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Запрос пользователя")
@allure.title("Успешный запрос пользователя по конкретному id")
def test_get_single_user():
    with allure.step('Отправка запроса и проверка на статус код'):
        response = requests.get(URL + '/users/11')
        assert response.status_code == 200

    response_json = response.json()

    with allure.step('Проверка соответствия запрошенного id и id пользователя'):
        text_value = response_json['data']['id']
        assert text_value == 11

    with allure.step('Валидация схемы json'):
        with open(f'{CURRENT_DIR}/schemas/single_user_schema.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)
