from shorty.services.exceptions import BadServiceName
from shorty.services import constants
from shorty.services.bitly import bitly_serv
from shorty.services.tinyurl import tinyurl_serv

DEFAULT_SERVICE = ["tinyurl"]
ACCEPTED_SERVICES = ["tinyurl", "bitly"]


class Services:
    """Args:
        this class combines the providers bitly and tinyurl
     """
    def __init__(self, data):
        self.provider = [data['provider'] if 'provider' in data else DEFAULT_SERVICE]
        self.url = data['url']

    def shortened_link(self):
        if self.provider[0] not in ACCEPTED_SERVICES:
            raise BadServiceName(self.provider[0])

        if self.provider == 'tinyurl':
            shorty = tinyurl_serv.tinyurlService(self.url).tinyurl_shortener()
        else:
            shorty = bitly_serv.bitlyService(self.url, constants.GENERIC_ACCESS_TOKEN).bitly_shortener()

        return shorty

