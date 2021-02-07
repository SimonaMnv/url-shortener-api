import requests


class bitlyService:
    """Args:
         url (str): the url you want to shorten
     Returns:
         str: the shortened url
     Raises:
         ResponseCodeStatusException: if the status code is not 200 (OK) then an exception is raised
     """
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def bitly_shortener(self):
        headers = {
            'Authorization': f"{self.token}",
            'Content-Type': 'application/json'
        }

        # have to get my account's group_guid
        group_guid = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
        group_guid = group_guid.json()['groups'][0]['guid']

        payload = {"long_url": f'{self.url}', "domain": "bit.ly", "group_guid": f'{group_guid}'}
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)

        if response.status_code != 200:
            return {"status_error": "service is unavailable right now"}

        return response.json()["link"]
