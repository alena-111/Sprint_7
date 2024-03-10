import requests
import conftest
import allure


class TestCreateCourier:
    @allure.title('Создание курьера')
    def test_create_courier(self, generate_courier_data):
        courier = generate_courier_data
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'password': courier[1],
                                       'firstName': courier[2]})
        assert response.status_code == 201

    # Комментарий в документации не соотв актуальному ответу
    @allure.title('Создание двух одинаковых курьеров')
    def test_two_identical_courier(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'password': courier[1],
                                       'firstName': courier[2]})
        assert response.json() == {"code": 409,
                                   "message": "Этот логин уже используется. Попробуйте другой."}

    # В документации нет обозначения обязательных полей
    @allure.title('Проверка на обязательные поля')
    def test_required_data(self, generate_courier_data):
        courier = generate_courier_data
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'firstName': courier[2]})
        assert response.status_code == 400

    @allure.title('Проверка кода ответа')
    def test_create_courier_status_code_201(self, generate_courier_data):
        courier = generate_courier_data
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'password': courier[1],
                                       'firstName': courier[2]})
        assert response.status_code == 201

    @allure.title('Проверка наличия в теле ответа ok-true')
    def test_create_courier_return_ok(self, generate_courier_data):
        courier = generate_courier_data
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'password': courier[1],
                                       'firstName': courier[2]})
        assert response.json() == {"ok": True}

    @allure.title('Отсутствие одного из обязательных полей в теле запроса')
    def test_missing_fields_data(self, generate_courier_data):
        courier = generate_courier_data
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'password': courier[1],
                                       'firstName': courier[2]})
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    @allure.title('Создание пользователя с логином, уже сущ. в базе')
    def test_same_login_courier(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier',
                                 data={'login': courier[0],
                                       'password': '1111',
                                       'firstName': 'Ivan'})
        assert response.json() == {"code": 409,
                                   "message": "Этот логин уже используется. Попробуйте другой."}
