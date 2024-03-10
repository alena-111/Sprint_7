import pytest
import requests
import random
import string
import allure

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture
@allure.title('Регистрация нового курьера')
def register_new_courier_and_return_login_password(generate_courier_data):
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # собираем тело запроса
    courier_data = generate_courier_data
    login = courier_data[0]
    password = courier_data[1]
    first_name = courier_data[2]

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + '/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@pytest.fixture
@allure.title('Генерация данных курьера')
def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data = []
    courier_data.append(login)
    courier_data.append(password)
    courier_data.append(first_name)

    return courier_data


@allure.title('Удаление курьера')
def delete_courier_data(login, password):
    data_courier = requests.post(
        BASE_URL + '/courier/login',
        data={'login': login, 'password': password})
    requests.delete(BASE_URL + '/courier/' + str(data_courier.json()['id']))


@pytest.fixture
@allure.title('Создание и удаление курьера')
def create_and_delete_courier(register_new_courier_and_return_login_password):
    courier = register_new_courier_and_return_login_password
    yield courier
    delete_courier_data(courier[0], courier[1])
