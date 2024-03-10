import pytest
import requests
import conftest
import allure


class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_order_list(self):
        response = requests.get(
            conftest.BASE_URL + '/orders?limit=2&page=0&nearestStation=["110"]')
        assert len(response.json()['orders']) == 2
