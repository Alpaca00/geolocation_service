from config_files import Configurator


class BasePage(object):

    conf = Configurator()

    def __init__(self):
        super(BasePage, self).__init__()
        self.base_url = self.conf.base_url
        self.new_url = self.conf.new_interface_url
        self.unk_url = self.conf.unk_url
        self.browser = None

    def open_new_url(self):
        self.browser.open(self.new_url)

    def login_as_user(self):
        pass

    def quit(self):
        self.browser.quit()
