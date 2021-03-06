Mission
-------

Your mission, should you choose to accept it, is to build a microservice called `shorty`, 
which supports two URL shortening providers: [bit.ly](https://dev.bitly.com/) and [tinyurl.com](https://gist.github.com/MikeRogers0/2907534).
You don't need to actually sign up to these providers, just implement their API. The
service exposes a single endpoint: `POST /shortlinks`. The endpoint should receive
JSON with the following schema:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The URL to shorten                 |
| provider | string | N        | The provider to use for shortening |

The response should be a `Shortlink` resource containing:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The original URL                   |
| link     | string | Y        | The shortened link                 |

For example:
```json
{
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka"
}
```

You are free to decide how to pick between the providers if one is not requested and what
your fallback strategy is in case your primary choice fails. Your endpoint needs to return
a JSON response with a sensible HTTP status in case of errors or failures.

Task
-------------------

1. Create a Python env (using Python 3.6+) and install the requirements.
2. Build the `POST /shortlinks` endpoint. We've provided a skeleton API using `flask`.
3. Write some tests. We've provided a test blueprint using `pytest`.

Resources
---------

1. `Flask`: http://flask.pocoo.org/
2. `pytest`: http://pytest.org/latest/
3. `virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/latest/
4. `HTTP statuses`: https://httpstatuses.com/

Implementation steps 
----------

1. `bitly & tinyurl`: Implemented tinyurl, bitly service classes, added a base class to combine them.
2. `POST /shortlinks`: Implemented the endpoint where the above classes are called based on user's input.
3. `error handling`: Implemented an error handler class and objects. 
3. `schema and provider control`: Set up a default provider if none is chosen. Implemented fallback strategy.
4. `unit testing`: Functions are tested.
5. `functional testing`: Flask server is tested.
6. `virtualenvwrapper`: Script added.
=======
