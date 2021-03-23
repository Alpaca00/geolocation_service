from selene import by
from selene.support.shared.jquery_style import s


class MainPage(object):
    def __init__(self):
        self.logo = s(by.xpath("//span[@class='x-tree-node-text  ']"))

