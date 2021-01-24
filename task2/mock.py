""" Mock объекты для тестирования сайта https://jsonplaceholder.typicode.com/ """


import requests


def get_photos():
    """ Mock ответ запроса сайта https://jsonplaceholder.typicode.com/"""

    return requests.get("https://jsonplaceholder.typicode.com/albums/1/photos/")


def mock_data_json():
    """ Возвращает пустой список """
    data = []

    return data
