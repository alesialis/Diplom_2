import helpers
import pytest
from helpers import *


class TestUserCreate:

    @allure.title('Корректное создание пользователя')
    @allure.description('При валидном запросе - ответ 200')
    def test_user_create_successful(self, generate_user_data):
        payload = generate_user_data
        response = helpers.post_create_user(payload)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Создание пользователя, который уже есть в системе')
    @allure.description('При запросе - ответ 403')
    def test_user_create_already_exists(self, create_user_login_then_delete):
        user_data, access_token = create_user_login_then_delete
        response = helpers.post_create_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == data.UNSUCCESSFUL_CREATE_USER_ALREADY_EXISTS

    @allure.title('Создание пользователя без обязательных полей')
    @allure.description('При запросе - ответ 403')
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_user_create_no_required_field(self, missing_field, generate_user_data):
        user_data = generate_user_data
        user_data.pop(missing_field)
        response = helpers.post_create_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == data.UNSUCCESSFUL_CREATE_USER_FIELD_REQUIRED

