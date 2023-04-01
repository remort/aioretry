# aioretry
Handy decorator to set retry policies for async callables with some handy features

# Usage examples

```
@retry(
    tries=5,
    allowed_exceptions=(RuntimeError,),
    intervals=(5, 7, 10),
    fail_cb=make_request_callback,
)
async def make_request(address, client):

    ... http request code goes here...

    if response.status_code >= 300:
        raise RuntimeError()

def make_request_callback(address, client)
    ...
```

- 5 retries will be performed
- with 5, 7, 10, 10 and 10 seconds interval between retries.
  I.e. if `intervals` tuple length more than `tries` number,
  the last tuple interval will be used for the rest of the tries.
- `make_request_callback()` synchronous function will be called if all attempts are failed
- The accepted exceptions tuple allows you to control when to retry.
- You can optionally pass a custom `logger: logging.Logger` to the decorator
  within a `logger=` parameter. Otherwise `retry_decorator` logger will be created to log retries.


Other possible ways to use this decorator:
```
@retry(5, (MyCustomError,), (5, 7, 10), make_request_callback)

@retry(3, (MyCustomError,), (1,))

# this actually will either successfully return or fail on first exception occured
@retry(3)
```

Look into `tests.py` to see more on usage.


# Install as package via pip

`pip install git+https://github.com/remort/aioretry.git#egg=aioretry_decorator`
