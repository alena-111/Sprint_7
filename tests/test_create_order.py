import pytest
import requests
import random
import string
import conftest
import allure


class TestCreateOrder:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('color',
                             [(['BLACK']), (['BLACK', 'GREY']), (['GREY']),
                              ([''])],
                             ids=['BLACK', 'BLACK and GREY',
                                  'GREY',
                                  'Without color'])
    def test_create_order(self, color):
        order = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
        order_color = {'color': color}
        response = requests.post(conftest.BASE_URL + '/orders',
                                 data=order.update(order_color))
        assert isinstance(response.json()['track'], int)
