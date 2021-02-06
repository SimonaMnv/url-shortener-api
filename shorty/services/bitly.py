import constants
import requests
import validators
from exceptions import (
    ResponseCodeStatusException,
    BadURLException
)

token = constants.GENERIC_ACCESS_TOKEN


class bitly:
    """Args:
         url (str): the url you want to shorten
     Returns:
         str: the shortened url
     Raises:
         ResponseCodeStatusException: if the status code is not 200 (OK) then an exception is raised
     """
    def bitly_shortener(self, url):
        headers = {
            'Authorization': f"{token}",
            'Content-Type': 'application/json'
        }

        # have to get my account's group_guid
        group_guid = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
        group_guid = group_guid.json()['groups'][0]['guid']

        payload = {"long_url": f'{url}', "domain": "bit.ly", "group_guid": f'{group_guid}'}
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)

        if response.status_code != 200:
            raise ResponseCodeStatusException(response.content)

        if not validators.url(url):
            raise BadURLException(url)

        return response.json()["link"]


bitly = bitly()
print(bitly.bitly_shortener("http://www.google.com/"))
