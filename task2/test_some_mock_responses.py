import pytest
import requests

from unittest.mock import Mock


@pytest.mark.parametrize("data , code_response", [
    ({
         'post_id': '1',
         'title': 'foo',
         'body': 'bar',
         'userId': '123'
     }, 200),
    ({
         'post_id': '000',
         'title': 'foo',
         'body': 'bar',
         'userId': '000'
     }, 404),
])
def test_update(start_url, data, code_response):
    post_id = data['post_id']
    res = requests.get(url=f'{start_url}/posts/{post_id}')
    assert res.status_code == code_response


def mock_server(
        *,
        json_data,
        status_code,
                ):
    response_mock = Mock()
    response_mock.status_code = status_code
    response_mock.json.return_value = json_data
    return response_mock


@pytest.mark.parametrize("data , code_response", [
    ({
         'post_id': '3',
         'title': 'foo',
         'body': 'bar',
         'userId': '789'
     }, 200),
    ({
         'post_id': '000',
         'title': 'foo',
         'body': 'bar',
         'userId': '000'
     }, 404),
])
def test_update_with_mock(data, code_response):
    res = mock_server(
        json_data=data,
        status_code=code_response
    )
    assert res.status_code == code_response
    assert res.json.return_value == data
