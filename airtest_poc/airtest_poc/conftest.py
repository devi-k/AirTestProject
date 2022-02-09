"""Base conftest.py."""
import pytest
from airtest.core.api import *
#@pytest.fixture(scope="session")
#@pytest.fixture(scope="module")
@pytest.fixture
def setup():
    init_device("Android")
    install("C:/Users/RH0539/Downloads/WorldWinner.apk")
    start_app("com.gsn.worldwinner")
    yield
    uninstall("com.gsn.worldwinner")

    





