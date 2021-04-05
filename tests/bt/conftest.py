import pytest
from selene.api import *

from src.bt_service_pages.login_page_bt import LoginPage
from src.domain.employee_bt import Employee


@pytest.fixture
def login_as_employee():
    user = Employee()
    email, password = user.find_email, user.find_password
    LoginPage().open().login_as(email, password)
    yield
    #browser.quit()
