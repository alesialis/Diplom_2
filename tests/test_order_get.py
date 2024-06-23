import helpers
from helpers import *


class TestOrderGet:

    @allure.title('Получение заказов пользователем с авторизацией')
    @allure.description('Ответ 200, в ответе валидные заказы')
    def test_order_get_user_with_authorization(self, create_user_login_then_delete, get_valid_ingredients):
        access_token = create_user_login_then_delete[1]
        order_payload = get_valid_ingredients
        helpers.post_create_order_with_token(order_payload, access_token)
        response_get_order = helpers.get_order_with_token(access_token)
        assert response_get_order.status_code == 200
        assert response_get_order.json()["success"] == True

    @allure.title('Получение заказов пользователем без авторизации')
    @allure.description('При запросе без авторизации - ответ 401')
    def test_order_get_user_without_authorization(self, create_user_login_then_delete, get_valid_ingredients):
        access_token = create_user_login_then_delete[1]
        order_payload = get_valid_ingredients
        helpers.post_create_order_with_token(order_payload, access_token)
        response_get_order = helpers.get_order_no_token()
        assert response_get_order.status_code == 401
        assert response_get_order.json()["message"] == data.NO_AUTHORIZATION_MESSAGE
