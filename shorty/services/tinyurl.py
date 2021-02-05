import requests
from exceptions import (
    ResponseCodeStatusException,
    BadURLException
)


class tinyurlService:
    def tinyurl_shortener(self, url):
        payload = {'url': url}
        response = requests.get("http://tinyurl.com/api-create.php", params=payload, timeout=5)
        if response.status_code != 200:
            raise ResponseCodeStatusException(response.content)

        return response.content.decode()


tinyurlService = tinyurlService()
print(tinyurlService.tinyurl_shortener("http://www.example.com/"))