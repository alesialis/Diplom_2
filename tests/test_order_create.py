import helpers
from helpers import *


class TestOrderCreate:

    @allure.title('Создание заказа пользователем с авторизацией и валидными ингредиентами')
    @allure.description('При валидном запросе - ответ 200')
    def test_order_create_user_with_authorization(self, create_user_login_then_delete, get_valid_ingredients):
        access_token = create_user_login_then_delete[1]
        order_payload = get_valid_ingredients
        response = helpers.post_create_order_with_token(order_payload, access_token)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Создание заказа пользователем без авторизации и валидными ингредиентами')
    @allure.description('При валидном запросе - ответ 200')
    def test_order_create_user_without_authorization(self, get_valid_ingredients):
        order_payload = get_valid_ingredients
        response = helpers.post_create_order_no_token(order_payload)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Создание заказа пользователем без авторизации без ингредиентов')
    @allure.description('При запросе без ингредиентов - ответ 400')
    def test_order_create_without_ingredients(self, create_user_login_then_delete):
        order_payload = []
        response = helpers.post_create_order_no_token(order_payload)
        assert response.status_code == 400
        assert response.json()["message"] == data.NO_INGREDIENTS_MESSAGE

    @allure.title('Создание заказа пользователем с авторизацией c невалидными ингредиентами')
    @allure.description('При запросе с невалидными ингредиентами - ответ 500')
    def test_order_create_incorrect_ingredients(self, create_user_login_then_delete):
        access_token = create_user_login_then_delete[1]
        order_payload = {
            "ingredients": [data.INCORRECT_INGREDIENT_1, data.INCORRECT_INGREDIENT_2]
            }
        response = helpers.post_create_order_with_token(order_payload, access_token)
        assert response.status_code == 500



