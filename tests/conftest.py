import pytest
import allure
from faker import Faker
import helpers


@allure.step('Генерация данных пользователя')
@pytest.fixture
def generate_user_data():
    faker = Faker()
    test_email = faker.email()
    test_password = faker.password()
    test_name = faker.name()
    user_data = {
        "email": test_email,
        "password": test_password,
        "name": test_name
    }
    return user_data


@allure.step('Создание пользователя, логин, удаление')
@pytest.fixture(scope="function")
def create_user_login_then_delete(generate_user_data):
    user_data = generate_user_data
    helpers.post_create_user(user_data)
    login_data = helpers.post_login_user(user_data).json()
    access_token = login_data["accessToken"]
    yield user_data, access_token
    helpers.delete_user(access_token, user_data)


@allure.step('Получение валидных ингедиентов')
@pytest.fixture(scope="function")
def get_valid_ingredients():
    response = helpers.get_ingredients()
    ingredients = response.json()["data"]
    first_ingredient = ingredients[0]["_id"]
    second_ingredient = ingredients[1]["_id"]
    payload = {
        "ingredients": [first_ingredient, second_ingredient]
    }
    return payload
