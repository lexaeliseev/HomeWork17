import json
import requests
import allure
from allure_commons.types import Severity
from jsonschema import validate
from resourses import CURRENT_DIR, URL

payload_miss_email = {
    "password": "qwerty"
}

error_email = 'Missing email or username'


@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Регистрация пользователя")
@allure.title("Не успешная регистрация пользователя")
def test_unsuccessful_register_user():
    with allure.step('Регистрация несуществующего пользователя и проверка на статус код'):
        response = requests.post(URL + '/register', json=payload_miss_email)
        assert response.status_code == 400

    response_json = response.json()

    with allure.step('Проверка отображения системной ошибки при пропущенном поле email'):
        assert response_json['error'] == error_email

    with allure.step('Валидация схемы json'):
        with open(f'{CURRENT_DIR}/schemas/unsuccessful_register_schema.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)
