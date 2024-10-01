from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_saml_providers_response_200 import ListSamlProvidersResponse200
from ...types import Response, Unset


def _get_kwargs(
    *,
    prefer: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(prefer, Unset):
        headers["Prefer"] = str(prefer)

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/saml",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListSamlProvidersResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListSamlProvidersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ListSamlProvidersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, ListSamlProvidersResponse200]]:
    """List SAML Providers

     List all registered SAML providers.

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListSamlProvidersResponse200]]
    """

    kwargs = _get_kwargs(
        prefer=prefer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, ListSamlProvidersResponse200]]:
    """List SAML Providers

     List all registered SAML providers.

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListSamlProvidersResponse200]
    """

    return sync_detailed(
        client=client,
        prefer=prefer,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, ListSamlProvidersResponse200]]:
    """List SAML Providers

     List all registered SAML providers.

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListSamlProvidersResponse200]]
    """

    kwargs = _get_kwargs(
        prefer=prefer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, ListSamlProvidersResponse200]]:
    """List SAML Providers

     List all registered SAML providers.

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListSamlProvidersResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            prefer=prefer,
        )
    ).parsed
