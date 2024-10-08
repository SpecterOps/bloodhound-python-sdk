# blood-hound-api-client
A client library for accessing BloodHound API

## Installing
The sdk can be installed from pypi with:

```
pip install blood-hound-python-client
```

## Usage
For HMAC authentication, create and copy your API Token id and key.

Create an HMACAuthenticationClient using your API Token id and key::

```python
import auth
from auth.hmac_authenticated_client import HMACAuthenticatedClient

token_key = "CAuAwLgPag3xpjfx5gYt3mEpRpK5DXkL1LGVK+utqMLTnlakVmjeZw=="
token_id = "5f538a38-fd90-4228-b17b-ee09056c6ade"
client = HMACAuthenticatedClient(base_url=base_url, token_key=token_key, token_id=token_id)

```

Now you can call your endpoint and use the model objects

Now call your endpoint and use your models:

```python

from blood_hound_api_client import AuthenticatedClient
from blood_hound_api_client.api.api_info import get_api_version
from blood_hound_api_client.models import GetApiVersionResponse200

with client as client::
    version: GetApiVersionResponse200 = get_api_version.sync(client=client)
    response: Response[GetApiVersionResponse200] = get_api_version.sync_detailed(client=client)
    print(f"version: {version.data.api}")
    print(f"response: {response}")

Or do the same thing with an async version:

```python
from blood_hound_api_client import AuthenticatedClient
from blood_hound_api_client.api.api_info import get_api_version
from blood_hound_api_client.models import GetApiVersionResponse200

async with client as client:
    version:: GetApiVersionResponse200 = await get_api_version.asyncio(client=client)
    response: Response[GetApiVersionResponse200] = await get_api_version.asyncio_detailed(client=client)
    print(f"version: {version.data.api}")
    print(f"response: {response}")

```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `blood_hound_api_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):


# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

## Building / publishing this package


This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
