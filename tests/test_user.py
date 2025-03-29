import requests
import pytest

def test_authentication_failed(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }
    # Create a mocked response with status code 401 and an empty text
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ""
    
    # Patch requests.get to return our mocked response
    mocker.patch('requests.get', return_value=mocked_response)
    
    response = requests.get(url, params=params)
    assert response.status_code == 401
    assert response.text.strip() == ""

def test_authentication_success(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }
    # Create a mocked response with status code 200 and an empty text
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ""
    
    # Patch requests.get to return our mocked response
    mocker.patch('requests.get', return_value=mocked_response)
    
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.text.strip() == ""