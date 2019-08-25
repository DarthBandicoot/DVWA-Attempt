import scrapy as scrapy
from loginform import fill_login_form

from constants import *


class DVWASpider(scrapy.Spider):
    name = 'dvwa_spider'
    sqli_characters = ["'", "\"", "`"]

    def __init__(self, *args, **kwargs):
        super(DVWASpider, self).__init__(*args, **kwargs)
        self.login_user = DVWA_LOGIN_USERNAME
        self.login_pass = DVWA_LOGIN_PASSWORD

    def start_requests(self):
        yield scrapy.Request(DVWA_BASE_URL + DVWA_LOGIN_PAGE, callback=self.login)

    def login(self, response):
        self.log("Attempting login to DVWA")
        try:
            data, url, method = fill_login_form(response.url,
                                                response.body,
                                                DVWA_LOGIN_USERNAME,
                                                DVWA_LOGIN_PASSWORD)
            yield scrapy.FormRequest(url,
                                     formdata=dict(data),
                                     method=method,
                                     callback=self.post_login)

        except Exception:
            return self.log("Login Failed")

    def post_login(self):
        pass

