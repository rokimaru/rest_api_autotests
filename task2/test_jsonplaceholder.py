""" Тесты api сайта https://jsonplaceholder.typicode.com/ """

import unittest
from unittest.mock import Mock, patch
from task2.methods import JsonSiteMethods
from task2.mock import get_photos, mock_data_json
import pytest
import requests
from nose.tools import assert_list_equal, assert_not_in


class TestJsonPlaceholderSite:
    """ Тесты api сайта https://jsonplaceholder.typicode.com/ """
    def test_jsonsite_get_1(self):
        """ Проверяем количество постов на сайте """
        response = requests.get('https://jsonplaceholder.typicode.com/posts',
                                headers=JsonSiteMethods.headers_data()).json()
        assert len(response) == 100

    def test_jsonsite_delete_2(self, ids_params):
        """ Проверяем, что можно удалить любой пост.
            Список ids можно указывать в переменной post_ids.
            Параметризация через фикстуру. """
        data = {
            "id": ids_params,
            "title": 'foo',
            "body": 'bar',
            "userId": 1}
        response = requests.delete('https://jsonplaceholder.typicode.com/posts/' + str(ids_params),
                                   json=data,
                                   headers=JsonSiteMethods.headers_data())
        assert response.status_code == 200

    def test_jsonsite_post_3(self):
        """ Проверка, что можно создать пост """
        data = {
            "title": 'foo',
            "body": 'bar',
            "userId": 1}
        response = requests.post('https://jsonplaceholder.typicode.com/posts/',
                                 json=data,
                                 headers=JsonSiteMethods.headers_data())

        assert response.json()["title"] == data["title"]
        assert response.json()["body"] == data["body"]
        assert response.json()["userId"] == data["userId"]
        assert response.json()["id"] > 100, print(response.json())

    def test_jsonsite_patch_4(self, ids_params):
        """ Проверяем, что можно заапдейтить любой пост.
            Список ids можно указывать в переменной post_ids.
            Параметризация через фикстуру."""
        data = {"title": 'foo'}
        response = requests.patch("https://jsonplaceholder.typicode.com/posts/" + str(ids_params),
                                  json=data,
                                  headers=JsonSiteMethods.headers_data())
        assert response.status_code == 200
        assert response.json()["title"] == data["title"]

    @pytest.mark.parametrize('ids_param', JsonSiteMethods.ids_list())
    def test_jsonsite_put_5(self, ids_param):
        """ Проверяем, что можно заапдейтить любой пост.
            Список ids можно указывать в переменной post_ids.
            Параметризация через декоратор."""
        data = {
            "id": ids_param,
            "title": 'foo',
            "body": 'bar',
            "userId": 1}
        response = requests.put("https://jsonplaceholder.typicode.com/posts/" + str(ids_param),
                                json=data,
                                headers=JsonSiteMethods.headers_data())
        assert response.status_code == 200
        assert response.json() == data


class UnittestJsonSite(unittest.TestCase):
    """ Тесты MOCK api сайта https://jsonplaceholder.typicode.com/ """

    def test_get_photo_if_server_is_ok(self):
        """ Проверка, что сервер не вернет ошибку, если в альбоме НЕТ фото """

        mock_data = mock_data_json()

        with patch('mock.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = mock_data
            response = get_photos()

            assert_list_equal(response.json(), mock_data)

    def test_get_photos_if_server_is_not_ok(self):
        """ Проверка, что сервер не вернет фото, когда НЕ доступен """

        with patch('mock.requests.get') as mock_get:
            mock_get.return_value.ok = False
            response = get_photos()

            assert_not_in("albumId", response)


if __name__ == '__main__':
    unittest.main()
