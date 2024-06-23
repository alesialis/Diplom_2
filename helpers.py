import allure
import requests
import data
import random
import string


@allure.step('Генерирация рандомной строки')
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

@allure.step('Запрос на создание пользователя')
def post_create_user(payload):
    request = requests.post(f'{data.URL + data.CREATE_USER_URL}', json=payload)
    return request


@allure.step('Запрос на удаление пользователя')
def delete_user(accessToken, payload):
    request = requests.delete(f'{data.URL + data.DELETE_USER_URL}', headers={"Authorization": accessToken}, json=payload)
    return request

@allure.step('Запрос на авторизацию пользователя')
def post_login_user(payload):
    request = requests.post(f'{data.URL + data.LOGIN_USER_URL}', json=payload)
    return request

@allure.step('Запрос на изменение данных пользователя')
def patch_change_user(accessToken, payload):
    request = requests.patch(f'{data.URL + data.UPDATE_USER_DATA_URL}', headers={"Authorization": accessToken}, json=payload)
    return request

@allure.step('Запрос на создание заказа без авторизации')
def post_create_order_no_token(payload):
    request = requests.post(f'{data.URL + data.CREATE_ORDER_URL}', json=payload)
    return request

@allure.step('Запрос на создание заказа с авторизацией')
def post_create_order_with_token(payload, accessToken):
    request = requests.post(f'{data.URL + data.CREATE_ORDER_URL}', headers={"Authorization": accessToken}, json=payload)
    return request

@allure.step('Запрос на получение заказа с авторизацией')
def get_order_with_token(accessToken):
    request = requests.get(f'{data.URL + data.GET_ORDER_URL}', headers={"Authorization": accessToken})
    return request

@allure.step('Запрос на получение заказа без авторизации')
def get_order_no_token():
    request = requests.get(f'{data.URL + data.GET_ORDER_URL}')
    return request

@allure.step('Запрос на получение ингредиентов')
def get_ingredients():
    request = requests.get(f'{data.URL + data.GET_INGREDIENTS_URL}')
    return request


