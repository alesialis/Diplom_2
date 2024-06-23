import helpers
import pytest
from helpers import *


class TestUserLogin:

    @allure.title('Корректный логин под существующим пользователем')
    @allure.description('При запросе - ответ 200')
    def test_user_login_successful(self, create_user_login_then_delete):
        user_data, access_token = create_user_login_then_delete
        response = helpers.post_login_user(user_data)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Логин под некорректным email и password')
    @allure.description('При запросе - ответ 200')
    @pytest.mark.usefixtures("create_user_login_then_delete")
    def test_login_with_incorrect_credentials(self, generate_user_data):
        user_data = generate_user_data
        user_data["email"] = helpers.generate_random_string(10)
        user_data["password"] = helpers.generate_random_string(10)
        response = helpers.post_login_user(user_data)
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == data.UNSUCCESSFUL_LOGIN_MESSAGE