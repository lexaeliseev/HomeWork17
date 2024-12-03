import requests
import allure
from allure_commons.types import Severity
from resourses import URL


@allure.tag("api")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Пользователь")
@allure.story("Удаление пользователя")
@allure.title("Успешное удаление пользователя")
def test_delete_user():
    with allure.step('Удаление существующего пользователя и проверка на статус код'):
        response = requests.delete(URL + '/users/4')
        assert response.status_code == 204