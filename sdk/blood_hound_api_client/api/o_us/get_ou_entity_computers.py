from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ou_entity_computers_type import GetOuEntityComputersType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    type: Union[Unset, GetOuEntityComputersType] = GetOuEntityComputersType.LIST,
    sort_by: Union[Unset, str] = UNSET,
    prefer: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(prefer, Unset):
        headers["Prefer"] = str(prefer)

    params: Dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["sort_by"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/ous/{object_id}/computers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    type: Union[Unset, GetOuEntityComputersType] = GetOuEntityComputersType.LIST,
    sort_by: Union[Unset, str] = UNSET,
    prefer: Union[Unset, int] = 0,
) -> Response[Any]:
    """Get OU entity computers

     Get a list, graph, or count of the computers contained by this OU.

    Args:
        object_id (str): The unique object identifier
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        type (Union[Unset, GetOuEntityComputersType]):  Default: GetOuEntityComputersType.LIST.
        sort_by (Union[Unset, str]): Sort by column. Can be used multiple times; prepend a hyphen
            for descending order.
            See parameter description for details about which columns are sortable.
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        skip=skip,
        limit=limit,
        type=type,
        sort_by=sort_by,
        prefer=prefer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    type: Union[Unset, GetOuEntityComputersType] = GetOuEntityComputersType.LIST,
    sort_by: Union[Unset, str] = UNSET,
    prefer: Union[Unset, int] = 0,
) -> Response[Any]:
    """Get OU entity computers

     Get a list, graph, or count of the computers contained by this OU.

    Args:
        object_id (str): The unique object identifier
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        type (Union[Unset, GetOuEntityComputersType]):  Default: GetOuEntityComputersType.LIST.
        sort_by (Union[Unset, str]): Sort by column. Can be used multiple times; prepend a hyphen
            for descending order.
            See parameter description for details about which columns are sortable.
        prefer (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        skip=skip,
        limit=limit,
        type=type,
        sort_by=sort_by,
        prefer=prefer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
