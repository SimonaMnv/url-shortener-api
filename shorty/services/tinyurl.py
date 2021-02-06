import requests
import validators
from exceptions import (
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
    def tinyurl_shortener(self, url):
        payload = {'url': url}
        response = requests.get("http://tinyurl.com/api-create.php", params=payload, timeout=5)

        if response.status_code != 200:
            raise ResponseCodeStatusException(response.content)

        if not validators.url(url):
            raise BadURLException(url)

        return response.content.decode()


tinyurlService = tinyurlService()
print(tinyurlService.tinyurl_shortener("http://www.google.com/"))