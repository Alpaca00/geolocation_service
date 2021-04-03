import pytest
from selene.support.shared import browser, config
from src.domain.employee_ukn import Admin
from src.ukn_service_pages.login_page import LoginPage




@pytest.fixture
def login_as_admin_unk():
    admin = Admin()
    email, password = admin.find_email_ukn, admin.find_password_ukn
    LoginPage().open().login_as(email, password)
    yield
    #browser.quit()

