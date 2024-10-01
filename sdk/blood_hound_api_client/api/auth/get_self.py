from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_authenticated_requester import ApiResponseAuthenticatedRequester
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
        "url": "/api/v2/self",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponseAuthenticatedRequester]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiResponseAuthenticatedRequester.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiResponseAuthenticatedRequester]]:
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
) -> Response[Union[Any, ApiResponseAuthenticatedRequester]]:
    """Get self

     Get the currently authenticated requester details. For Community, this will only ever be valid for
    users. In Enterprise, this could be either a BloodHound user or a client (collector).

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseAuthenticatedRequester]]
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
) -> Optional[Union[Any, ApiResponseAuthenticatedRequester]]:
    """Get self

     Get the currently authenticated requester details. For Community, this will only ever be valid for
    users. In Enterprise, this could be either a BloodHound user or a client (collector).

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseAuthenticatedRequester]
    """

    return sync_detailed(
        client=client,
        prefer=prefer,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, ApiResponseAuthenticatedRequester]]:
    """Get self

     Get the currently authenticated requester details. For Community, this will only ever be valid for
    users. In Enterprise, this could be either a BloodHound user or a client (collector).

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseAuthenticatedRequester]]
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
) -> Optional[Union[Any, ApiResponseAuthenticatedRequester]]:
    """Get self

     Get the currently authenticated requester details. For Community, this will only ever be valid for
    users. In Enterprise, this could be either a BloodHound user or a client (collector).

    Args:
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseAuthenticatedRequester]
    """

    return (
        await asyncio_detailed(
            client=client,
            prefer=prefer,
        )
    ).parsed
