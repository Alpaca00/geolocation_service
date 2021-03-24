from selene.support import by
from selene.support.shared.jquery_style import s


class MileageReportPageLocators:
    LOGO = "//*[@id='ext-element-11']"


class MileageReportPage(MileageReportPageLocators):

    def __init__(self):
        super(MileageReportPage).__init__()

    def logo_text(self):
        return s(by.xpath(self.LOGO))
