import requests
import validators
from shorty.services.exceptions import (
    ResponseCodeStatusException,
    BadURLException
)


class tinyurlService:
    """Args:
         url (str): the url you want to shorten
     Returns:
         str: the shortened url
     Raises:
         ResponseCodeStatusException: if the status code is not 200 (OK) then an exception is raised
     """
    def __init__(self, url):
        self.url = url

    def tinyurl_shortener(self):
        payload = {'url': self.url}
        response = requests.get("http://tinyurl.com/api-create.php", params=payload, timeout=5)

        if response.status_code != 200:
            raise ResponseCodeStatusException(response.content)

        if not validators.url(self.url):
            raise BadURLException(self.url)

        return response.content.decode()
