from shorty.services import constants
from shorty.services.bitly import bitly_serv
from shorty.services.tinyurl import tinyurl_serv
import validators

DEFAULT_SERVICE = "tinyurl"
ACCEPTED_SERVICES = ["tinyurl", "bitly"]


class Services:
    """ this class combines the providers bitly and tinyurl """
    def __init__(self, data):
        self.provider = [data['provider'] if 'provider' in data else DEFAULT_SERVICE]
        self.url = data['url']

    def wrong_url(self):
        if not validators.url(self.url):
            return True
        return False

    def wrong_provider(self):
        if self.provider[0] not in ACCEPTED_SERVICES:
            return True
        return False

    def shortened_link(self):
        shorty = ""
        if self.provider[0] == 'tinyurl':
            shorty = tinyurl_serv.tinyurlService(self.url).tinyurl_shortener()
            if shorty == {"status_error": "service is unavailable right now"}:
                shorty = bitly_serv.bitlyService(self.url, constants.GENERIC_ACCESS_TOKEN).bitly_shortener()
        elif self.provider[0] == 'bitly':
            shorty = bitly_serv.bitlyService(self.url, constants.GENERIC_ACCESS_TOKEN).bitly_shortener()
            if shorty == {"status_error": "service is unavailable right now"}:
                shorty = tinyurl_serv.tinyurlService(self.url).tinyurl_shortener()

        return {"url": self.url, "link": shorty}

