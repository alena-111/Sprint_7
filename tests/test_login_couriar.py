import requests
import conftest
import allure
import data.data as test_data


class TestLoginCourier:

    @allure.title('Авторизация курьера')
    def test_login_courier_succes(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'login': courier[0],
                                       'password': courier[1]
                                       })
        assert response.status_code == 200

    @allure.title('Проверка обязательных полей для авторизации')
    def test_login_courier_without_password(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'password': courier[1]
                                       })
        assert response.json() == test_data.LOGIN_COURIER_INCORRECT_DATA_400

    @allure.title('Авторизация с невалидным логином')
    def test_login_courier_incorrect_login(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'login': ' ',
                                       'password': courier[1]
                                       })
        assert response.json() == test_data.LOGIN_COURIER_INCORRECT_LOGIN_404

    @allure.title('Авторизация без обязательного поля (пароля)')
    def test_login_courier_incorrect_password(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'login': courier[0],
                                       'password': ' '
                                       })
        assert response.json() == test_data.LOGIN_COURIER_INCORRECT_LOGIN_404

    @allure.title('Авторизация без обязательного поля (логин)')
    def test_login_courier_without_login(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'password': courier[1]
                                       })
        assert response.json() == test_data.LOGIN_COURIER_INCORRECT_DATA_400

    @allure.title('Авторизация под незарегестрированным пользователем')
    def test_login_courier_does_not_exist(self):
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'login': '',
                                       'password': ''
                                       })
        assert response.json() == test_data.LOGIN_COURIER_INCORRECT_DATA_400

    @allure.title('Получение id курьера')
    def test_login_courier_returns_id(self, create_and_delete_courier):
        courier = create_and_delete_courier
        response = requests.post(conftest.BASE_URL + '/courier/login',
                                 data={'login': courier[0],
                                       'password': courier[1]
                                       })
        assert isinstance(response.json()['id'], int)
