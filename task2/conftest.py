""" https://jsonplaceholder.typicode.com/ """

import pytest


@pytest.fixture(params=list(range(1, 11)))
def ids_params(request):
    """ Фикстура возвращает список ids постов """
    return request.param
