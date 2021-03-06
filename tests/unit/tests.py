import unittest
from shorty.services.base import Services
from shorty.services.error_handler import CustomError

VALID_INPUT_DATA = {
    "url": "https://google.com",
    "provider": "tinyurl"
}

VALID_INPUT_DATA_ = {
    "url": "https://www.google.com/search?q=flask&sxsrf=ALeKk02e-H84ZfpM2lOTrVqFrDUzTPru1A:1612734244896&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiSzaKe39juAhXFxoUKHVWEBMQQ_AUoAXoECBkQAw#imgrc=m5f1VW-NaZVp2M",
}

INVALID_INPUT_DATA = {
    "url": "htps://google.com",
    "provider": "tinyurl"
}

INVALID_INPUT_DATA_ = {
    "url": "https://google.com",
    "provider": "tinyur1"
}

INVALID_INPUT_DATA__ = {
    "url": "htps://google.com",
    "provider": "tinyur1"
}

INVALID_PARAMS = {
    "wrong": "htps://google.com",
    "provider": "tinyurl"
}


class ShortyUnitTest(unittest.TestCase):
    """ testing a small piece of code or a function/method to check whether it is working fine or not """

    def test_url_wrong(self):
        with self.assertRaises(CustomError) as context:
            Services(INVALID_INPUT_DATA).check_url_invalid_format()

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.error_message, "URL is not valid")

    def test_wrong_provider(self):
        with self.assertRaises(CustomError) as context:
            Services(INVALID_INPUT_DATA_).check_provider_invalid_format()

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.error_message, "Provider parameter is not valid")

    def test_wrong_provider_and_url(self):
        with self.assertRaises(CustomError) as context:
            Services(INVALID_INPUT_DATA__).check_url_and_provider_invalid_format()

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.error_message, "Both provider and URL are not valid")

    def test_wrong_parameters(self):
        with self.assertRaises(CustomError) as context:
            Services(INVALID_PARAMS).check_url_and_provider_invalid_format()

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.error_message, "URL parameter not found")

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
