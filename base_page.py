from config_files import Configurator


class BasePage(object):

    conf = Configurator()

    def __init__(self):
        super(BasePage, self).__init__()
        self.base_url = self.conf.base_url
        self.page_url = None
