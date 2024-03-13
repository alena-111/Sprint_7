import pytest
import requests
import conftest
import allure
import data.data as test_data


class TestCreateOrder:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('color',
                             [(['BLACK']), (['BLACK', 'GREY']), (['GREY']),
                              ([''])],
                             ids=['BLACK', 'BLACK and GREY',
                                  'GREY',
                                  'Without color'])
    def test_create_order(self, color):
        order = test_data.ORDER
        order_color = {'color': color}
        response = requests.post(conftest.BASE_URL + '/orders',
                                 data=order.update(order_color))
        assert isinstance(response.json()['track'], int)
