""" https://dog.ceo/ """

import pytest
import requests
import methods


class TestDogSite:
    """ Тесты api сайта https://dog.ceo/"""
    def test_dogsite_number_of_breeds_1(self):
        """ Количество пород на сайте = 92"""
        assert len(methods.DogSiteMethods.get_all_breeds()) == 92

    def test_dogsite_breeds_list_format_2(self):
        """ Список пород получается в формате json"""
        response = (requests.get('https://dog.ceo/api/breeds/list/all'))
        assert response.headers['Content-Type'] == 'application/json'

    def test_dogsite_breeds_list_success_3(self):
        """ Список пород приходит со статусом "success" """
        response = requests.get('https://dog.ceo/api/breeds/list/all').json()
        assert response['status'] == 'success'

    @pytest.mark.parametrize('breed_list', methods.DogSiteMethods.get_all_breeds())
    def test_dogsite_random_image_for_breed_4(self, breed_list):
        """ Запрос рандомного изображения для каждой породы успешен.
            Параметризация через декоратор. """
        response = methods.DogSiteMethods.request_breed_image(breed_list)
        assert response.status_code == 200

    def test_dogsite_every_breed_has_an_image_5(self, breed_list):
        """ У каждой породы есть минимум 1 фото.
            Параметризация через фикстуру."""
        response = methods.DogSiteMethods.request_breed_image(breed_list)
        assert response.json()['message'] is not None
