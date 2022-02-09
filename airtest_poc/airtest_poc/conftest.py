# -*- encoding=utf8 -*-
"""Base conftest.py."""

import pytest
from airtest.core.settings import Settings as ST
from airtest.core.helper import set_logdir
from airtest.core.api import *
from airtest.report.report import *
from airtest.report.report import simple_report
auto_setup(__file__, logdir=True)
import os

ST.LOG_FILE = "log.txt"
set_logdir(r'C:\Users\RH0539\Desktop\AirTestProject\airtest_poc\airtest_poc\proj_test\tests\Login_test.air\log')

#@pytest.fixture(scope="session")
#@pytest.fixture(scope="module")
@pytest.fixture
def setup():
    init_device("Android")
    install("C:/Users/RH0539/Downloads/WorldWinner.apk")
    start_app("com.gsn.worldwinner")
    
    yield
    simple_report(__file__,logpath=True,logfile=r"C:\Users\RH0539\Desktop\AirTestProject\airtest_poc\airtest_poc\proj_test\tests\Login_test.air\log\log.txt",output=r"C:\Users\RH0539\Desktop\AirTestProject\airtest_poc\airtest_poc\proj_test\tests\Login_test.air\log\report.html")
    uninstall("com.gsn.worldwinner")

    





