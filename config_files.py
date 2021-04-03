import configparser


class Configurator:

    config = configparser.ConfigParser(interpolation=None)
    config.read('/home/oleg/python/geolocation_service/config.ini', encoding='utf-8')

    def __init__(self):
        super(Configurator, self)
        self.base_url = self.config['web_pages']['base_url']
        self.new_interface_url = self.config['web_pages']['new_interface_url']
        self.unk_url = self.config['web_pages']['unk_url']
