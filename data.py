# url и endpoint
URL = 'https://stellarburgers.nomoreparties.site'
CREATE_USER_URL = '/api/auth/register'
DELETE_USER_URL = '/api/auth/user'
LOGIN_USER_URL = '/api/auth/login'
UPDATE_USER_DATA_URL = '/api/auth/user'
CREATE_ORDER_URL = '/api/orders'
GET_ORDER_URL = '/api/orders'
GET_INGREDIENTS_URL = '/api/ingredients'


# тексты в ответах на запросы
UNSUCCESSFUL_CREATE_USER_ALREADY_EXISTS = "User already exists"
UNSUCCESSFUL_CREATE_USER_FIELD_REQUIRED = "Email, password and name are required fields"
UNSUCCESSFUL_LOGIN_MESSAGE = "email or password are incorrect"
NO_AUTHORIZATION_MESSAGE = "You should be authorised"
NO_INGREDIENTS_MESSAGE = "Ingredient ids must be provided"


# тестовые данные
INCORRECT_INGREDIENT_1 = "test_ingredient"
INCORRECT_INGREDIENT_2 = "тестовый-ингредиент123"



