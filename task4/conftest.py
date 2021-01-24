import pytest


def pytest_addoption(parser):
    parser.addoption('--url', type=str, default='https://ya.ru')
    parser.addoption('--status_code', type=int, default=200)


@pytest.fixture
def get_options(request):
    return (request.config.getoption('--url'),
            request.config.getoption('--status_code'))