import json
import requests
import allure
from allure_commons.types import Severity
from jsonschema import validate
from resourses import CURRENT_DIR, URL

payload = {
    "name": "lexaeliseev",
    "job": "QA"
}

@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Создание пользователя")
@allure.title("Успешное создание пользователя")
def test_create_user():
    with allure.step('Создание пользователя и проверка на статус код'):
        response = requests.post(URL + '/users', data=payload)
        assert response.status_code == 201

    response_json = response.json()

    with allure.step('Проверка корректности созданного пользователя'):
        text_name = response_json['name']
        text_job = response_json['job']
        assert text_name == payload['name']
        assert text_job == payload['job']
        print(response_json)

    with allure.step(' Валидация схемы json'):
        with open(f'{CURRENT_DIR}/schemas/create_user_schema.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)