from shorty.app import create_app

VALID_URL = "https://google.com"
VALID_PROVIDER = "tinyurl"

INVALID_URL = "htps://google.com"
INVALID_PROVIDER = "tinyurl1"

VALID_INPUT_DATA = {
    "url": VALID_URL,
    "provider": VALID_PROVIDER
}

VALID_INPUT_DATA_ = {
    "url": VALID_URL
}

INVALID_INPUT_DATA = {
    "url": INVALID_URL,
    "provider": INVALID_PROVIDER
}

INVALID_INPUT_URL = {
    "url": INVALID_URL,
    "provider": VALID_PROVIDER
}

INVALID_INPUT_URL_ = {
    "url": "",
    "provider": VALID_PROVIDER
}

INVALID_INPUT_URL__ = {
    "provider": VALID_PROVIDER
}

INVALID_INPUT_PROVIDER = {
    "url": VALID_URL,
    "provider": INVALID_PROVIDER
}


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_endpoint_post_valid(post):
    """Test that the flask server is running and reachable. test all endpoint valid data combinations """
    res = post('/shortlinks', data=VALID_INPUT_DATA)
    res_ = post('/shortlinks', data=VALID_INPUT_DATA_)
    assert res.status_code == 200
    assert res.get_json() is not None
    assert res.get_json()['link'] is not None
    assert res.get_json()['url'] is not None
    assert res.get_json()['url'] == VALID_URL

    assert res_.status_code == 200
    assert res_.get_json() is not None
    assert res_.get_json()['link'] is not None
    assert res_.get_json()['url'] is not None
    assert res_.get_json()['url'] == VALID_URL


def test_endpoint_post_invalid(post):
    """ test post-invalid provider and url case """
    res = post('/shortlinks', data=INVALID_INPUT_DATA)
    res_ = post('/shortlinks', data={})
    assert res.status_code == 400
    assert res.get_json() == {
        "error_message": "Both provider and URL are not valid",
        "status_code": 400,
        "suggested_action": "valid URL example: https://google.com, valid provider examples: bitly, tinyurl"
    }

    assert res_.status_code == 400
    assert res_.get_json() == {
        "error_message": "JSON body is empty",
        "status_code": 400,
        "suggested_action": "fill JSON body"
    }


def test_endpoint_post_invalid_url(post):
    """ test post-invalid url case """
    res = post('/shortlinks', data=INVALID_INPUT_URL)
    res_ = post('/shortlinks', data=INVALID_INPUT_URL_)
    res__ = post('/shortlinks', data=INVALID_INPUT_URL__)
    assert res.status_code == 400
    assert res.get_json() == {
        "error_message": "URL is not valid",
        "status_code": 400,
        "suggested_action": "valid example: https://google.com"
    }

    assert res_.status_code == 400
    assert res_.get_json() == {
        "error_message": "URL is not valid",
        "status_code": 400,
        "suggested_action": "valid example: https://google.com"
    }

    assert res__.status_code == 400
    assert res__.get_json() == {
        "error_message": "URL parameter not found",
        "status_code": 400,
        "suggested_action": "add URL parameter"
    }


def test_endpoint_post_invalid_provider(post):
    """ test post-invalid provider case """
    res = post('/shortlinks', data=INVALID_INPUT_PROVIDER)
    assert res.status_code == 400
    assert res.get_json() == {
        "error_message": "Provider parameter is not valid",
        "status_code": 400,
        "suggested_action": "tinyurl or bitly"
    }


def test_endpoint_get(get):
    """Test that get request is not allowed"""
    res = get('/shortlinks', data=VALID_INPUT_DATA)
    assert res.status_code == 405
