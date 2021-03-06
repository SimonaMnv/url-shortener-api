import requests


class TinyUrlService:
    """Args:
         url (str): the url you want to shorten
     Returns:
         str: the shortened url
     Raises:
         ResponseCodeStatusException: if the status code is not 200 (OK) then an exception is raised
     """
    def __init__(self, url):
        self.url = url
        self.available = True

    def tinyurl_shortener(self):
        payload = {'url': self.url}
        response = requests.get("http://tinyurl.com/api-create.php", params=payload, timeout=5)

        if response.status_code != 200:
            self.available = False
            return self.available

        return response.content.decode()
