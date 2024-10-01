from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_client_info_body import UpdateClientInfoBody
from ...models.update_client_info_response_200 import UpdateClientInfoResponse200
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: UpdateClientInfoBody,
    prefer: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(prefer, Unset):
        headers["Prefer"] = str(prefer)

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/clients/update",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateClientInfoResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateClientInfoResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateClientInfoResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateClientInfoBody,
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, UpdateClientInfoResponse200]]:
    """Update Client Values

     Endpoint for clients to update their own information at startup.

    Note: caller must be a client. For users, this endpoint will return a 404 as
    they are not expected or allowed to call this endpoint.

    Args:
        prefer (Union[Unset, int]):  Default: 0.
        body (UpdateClientInfoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateClientInfoResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        prefer=prefer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateClientInfoBody,
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, UpdateClientInfoResponse200]]:
    """Update Client Values

     Endpoint for clients to update their own information at startup.

    Note: caller must be a client. For users, this endpoint will return a 404 as
    they are not expected or allowed to call this endpoint.

    Args:
        prefer (Union[Unset, int]):  Default: 0.
        body (UpdateClientInfoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateClientInfoResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        prefer=prefer,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateClientInfoBody,
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, UpdateClientInfoResponse200]]:
    """Update Client Values

     Endpoint for clients to update their own information at startup.

    Note: caller must be a client. For users, this endpoint will return a 404 as
    they are not expected or allowed to call this endpoint.

    Args:
        prefer (Union[Unset, int]):  Default: 0.
        body (UpdateClientInfoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateClientInfoResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        prefer=prefer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateClientInfoBody,
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, UpdateClientInfoResponse200]]:
    """Update Client Values

     Endpoint for clients to update their own information at startup.

    Note: caller must be a client. For users, this endpoint will return a 404 as
    they are not expected or allowed to call this endpoint.

    Args:
        prefer (Union[Unset, int]):  Default: 0.
        body (UpdateClientInfoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateClientInfoResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            prefer=prefer,
        )
    ).parsed
