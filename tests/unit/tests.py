import unittest
from shorty.services.base import Services

VALID_INPUT_DATA = {
    "url": "https://google.com",
    "provider": "tinyurl"
}

VALID_INPUT_DATA_ = {
    "url": "https://www.google.com/search?q=flask&sxsrf=ALeKk02e-H84ZfpM2lOTrVqFrDUzTPru1A:1612734244896&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiSzaKe39juAhXFxoUKHVWEBMQQ_AUoAXoECBkQAw#imgrc=m5f1VW-NaZVp2M",
}

INVALID_INPUT_DATA = {
    "url": "htps://google.com",
    "provider": "tinyur1"
}


class ShortyUnitTest(unittest.TestCase):
    """ testing a small piece of code or a function/method to check whether it is working fine or not """

    def test_url_wrong(self):
        res = Services(INVALID_INPUT_DATA).wrong_url()
        self.assertEqual(res, True)

    def test_wrong_provider(self):
        res = Services(INVALID_INPUT_DATA).wrong_provider()
        self.assertEqual(res, True)

    def test_url_valid(self):
        res = Services(VALID_INPUT_DATA).wrong_url()
        self.assertEqual(res, False)

    def test_provider_valid(self):
        res = Services(VALID_INPUT_DATA).wrong_provider()
        self.assertEqual(res, False)

    def test_long_url(self):
        res = Services(VALID_INPUT_DATA_).wrong_url()
        self.assertEqual(res, False)

    def test_empty_provider(self):
        res = Services(VALID_INPUT_DATA_).wrong_provider()
        self.assertEqual(res, False)

    def test_shortened_link_valid(self):
        res = Services(VALID_INPUT_DATA).shortened_link()
        self.assertGreater(len(res['link']), 0)

    def test_shortened_link_valid_(self):
        res = Services(VALID_INPUT_DATA_).shortened_link()
        self.assertGreater(len(res['link']), 0)

    def test_shortened_link_invalid(self):
        res = Services(INVALID_INPUT_DATA).shortened_link()
        self.assertEqual(len(res['link']), 0)


if __name__ == '__main__':
    unittest.main()
