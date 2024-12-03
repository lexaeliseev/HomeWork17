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
@allure.title("Отображение ошибки при запросе пользователя с несуществующим id")
def test_get_single_user_not_found():
    with allure.step('Отправка некорректного запроса и проверка его на статус код'):
        response = requests.get(URL + '/users/2000')
        assert response.status_code == 404

    response_json = response.json()

    with allure.step('Проверка тела ответа'):
        text_value = response_json
        assert text_value == {}

    with allure.step('Валидация схемы json'):
        with open(f'{CURRENT_DIR}/schemas/single_user_not_found.json') as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)