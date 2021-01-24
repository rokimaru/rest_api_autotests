""" Фикстуры для автотестов сайта https://api.openbrewerydb.org/ """

import pytest
from task3.methods import BrewerySiteMethods


@pytest.fixture(params=['Dog', 'Beer', 'House', 'Mom', 'England'])
def brewery_name(request):
    """ Фикстура возвращает список name пивоварен """
    return request.param


@pytest.fixture(params=BrewerySiteMethods.get_all_breweries_id())
def brewery_id(request):
    """ Фикстура возвращает список id пивоварен на 1 странице """
    return request.param


@pytest.fixture(params=['micro', 'regional', 'brewpub',
                        'large', 'planning', 'bar',
                        'contract', 'proprietor'])
def brewery_type(request):
    """ Фикстура возвращает список type пивоварен """
    return request.param
