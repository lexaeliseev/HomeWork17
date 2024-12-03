import json
import requests
import allure
from allure_commons.types import Severity
from jsonschema import validate
from resourses import CURRENT_DIR, URL

payload = {
    "name": "КУРЛЫК",
    "job": "AQA"
}


@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Обновление пользователя")
@allure.title("Успешное полное обновление пользователя")
def test_update_put_user():
    with allure.step('Обновление существующего пользователя и проверка на статус код'):
        response = requests.put(URL + '/users/867', data=payload)
        assert response.status_code == 200

    response_json = response.json()

    with allure.step('Проверка корректности созданного пользователя'):
        text_name = response_json['name']
        text_job = response_json['job']
        assert text_name == payload['name']
        assert text_job == payload['job']
        assert 'updatedAt' in response_json

    with allure.step('Валидация схемы json'):
        with open(f'{CURRENT_DIR}/schemas/update_user_schema.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)