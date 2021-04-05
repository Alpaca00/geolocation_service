import pytest
from src.bt_service_pages.login_page_bt import LoginPage
from src.domain.employee_bt import Employee


@pytest.mark.skip()
def test_can_emp_login():
    user = Employee()
    email, password = user.find_email, user.find_password
    LoginPage().open().login_as(email, password)
