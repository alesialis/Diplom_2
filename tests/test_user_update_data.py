import helpers
import pytest
from helpers import *
import data


class TestUserUpdateData:

    @allure.title('Корректное изменение данных пользователя с авторизацией')
    @allure.description('При запросе - ответ 200')
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_update_user_data_with_authorization(self, create_user_login_then_delete, field):
        user_data, access_token = create_user_login_then_delete
        payload = {field: helpers.generate_random_string(10)}
        response = helpers.patch_change_user(access_token, payload)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Нельзя изменить данные пользователя без авторизации')
    @allure.description('При запросе - ответ 200')
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_update_user_data_without_authorization(self, field):
        payload = {field: helpers.generate_random_string(10)}
        response = helpers.patch_change_user("", payload)
        assert response.status_code == 401
        assert response.json()["message"] == data.NO_AUTHORIZATION_MESSAGE