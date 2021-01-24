""" Тесты api сайта https://www.openbrewerydb.org/ """

import pytest
import requests
from task3.methods import BrewerySiteMethods


class TestJsonPlaceholderSite:
    """ Тесты api сайта https://www.openbrewerydb.org/ """

    def test_openbrewerydb_1(self):
        """ Проверка, что общее количество пивоварен на 1 странице = 20 """
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        assert len(response) == 20

    def test_openbrewerydb_2(self, brewery_type):
        """ Проверка фильтрации по brewery_type"""
        response = requests.get('https://api.openbrewerydb.org/breweries?by_type=' + brewery_type)
        assert response.status_code == 200
        assert response.json()[0]["brewery_type"] == brewery_type

    def test_openbrewerydb_3(self, brewery_name):
        """ Проверка, фильтрации пивоварен по name """
        response = requests.get("https://api.openbrewerydb.org/breweries?by_name=" + brewery_name)
        assert response.status_code == 200
        assert brewery_name in response.json()[0]["name"]

    def test_openbrewerydb_4(self, brewery_id):
        """ Проверяем, что можно получить инфо о любой пивоварне по id.
            Тест через фикстуру."""
        response = BrewerySiteMethods.request_brewery_information(brewery_id)
        assert response.status_code == 200
        assert response.json()["id"] == brewery_id

    @pytest.mark.parametrize('ids_param', BrewerySiteMethods.get_all_breweries_id())
    def test_openbrewerydb_5(self, ids_param):
        """ Проверяем, что можно получить инфо о любой пивоварне по id.
            Тест через маркер pytest"""
        response = requests.get('https://api.openbrewerydb.org/breweries/' + str(ids_param))
        assert response.status_code == 200
        assert response.json()["id"] == ids_param
