import pytest
import requests

x = requests.get('https://google.com')

def test_1():
    assert x.status_code == 200

