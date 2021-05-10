class BasePage:
    def __init__(self, _driver, _url):
        self.driver = _driver
        self.url = _url

    def open(self):
        self.driver.get(self.url)
