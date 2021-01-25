""" https://dog.ceo/api/breed/ """

import pytest
from task1.methods import DogSiteMethods


@pytest.fixture(params=DogSiteMethods.get_all_breeds())
def breed_list(request):
    """ Фикстура возвращает список всех пород собак """
    return request.param
