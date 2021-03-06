from shorty.services import constants
from shorty.services.bitly.bitly_serv import BitlyService
from shorty.services.tinyurl.tinyurl_serv import TinyUrlService
import validators
from shorty.services import error_handler


DEFAULT_SERVICE = "tinyurl"
ACCEPTED_SERVICES = ["tinyurl", "bitly"]


class Services:
    """ this class combines the providers bitly and tinyurl """
    def __init__(self, data):
        self.provider = data['provider'] if 'provider' in data else DEFAULT_SERVICE
        self.url = data['url']
        self.data_keys = list(data.keys())
        self.shorty = ""

    def check_request_parameters_format(self):
        if [True for key in self.data_keys if key not in ['provider', 'url']]:
            raise error_handler.wrong_request_parameters()

    def check_url_and_provider_invalid_format(self):
        if (not validators.url(self.url)) and (self.provider not in ACCEPTED_SERVICES):
            raise error_handler.url_provider_invalid_format()

    def check_url_invalid_format(self):
        if not validators.url(self.url):
            raise error_handler.url_invalid_format()

    def check_provider_invalid_format(self):
        if self.provider not in ACCEPTED_SERVICES:
            raise error_handler.invalid_provider()

    def check_errors(self):
        self.check_url_and_provider_invalid_format()
        self.check_url_invalid_format()
        self.check_provider_invalid_format()
        self.check_request_parameters_format()

    def shortened_link(self):
        if self.provider == "bitly":
            self.shorty = BitlyService(self.url, constants.GENERIC_ACCESS_TOKEN).bitly_shortener()
            if not self.shorty:
                self.shorty = TinyUrlService(self.url).tinyurl_shortener()
                if not self.shorty:
                    raise error_handler.both_services_down()

        if self.provider == "tinyurl":
            self.shorty = TinyUrlService(self.url).tinyurl_shortener()
            if not self.shorty:
                self.shorty = BitlyService(self.url, constants.GENERIC_ACCESS_TOKEN).bitly_shortener()
                if not self.shorty:
                    raise error_handler.both_services_down()

        return {"url": self.url, "link": self.shorty}
