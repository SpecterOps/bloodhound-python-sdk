from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_asset_group_selector_spec import ModelAssetGroupSelectorSpec
from ...models.update_asset_group_selectors_deprecated_response_201 import (
    UpdateAssetGroupSelectorsDeprecatedResponse201,
)
from ...types import Response, Unset


def _get_kwargs(
    asset_group_id: int,
    *,
    body: List["ModelAssetGroupSelectorSpec"],
    prefer: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(prefer, Unset):
        headers["Prefer"] = str(prefer)

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/asset-groups/{asset_group_id}/selectors",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UpdateAssetGroupSelectorsDeprecatedResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["ModelAssetGroupSelectorSpec"],
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    """Update asset group selectors

     DEPRECATED use PUT instead. Updates asset group selectors.

    Args:
        asset_group_id (int):
        prefer (Union[Unset, int]):  Default: 0.
        body (List['ModelAssetGroupSelectorSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]
    """

    kwargs = _get_kwargs(
        asset_group_id=asset_group_id,
        body=body,
        prefer=prefer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["ModelAssetGroupSelectorSpec"],
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    """Update asset group selectors

     DEPRECATED use PUT instead. Updates asset group selectors.

    Args:
        asset_group_id (int):
        prefer (Union[Unset, int]):  Default: 0.
        body (List['ModelAssetGroupSelectorSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]
    """

    return sync_detailed(
        asset_group_id=asset_group_id,
        client=client,
        body=body,
        prefer=prefer,
    ).parsed


async def asyncio_detailed(
    asset_group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["ModelAssetGroupSelectorSpec"],
    prefer: Union[Unset, int] = 0,
) -> Response[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    """Update asset group selectors

     DEPRECATED use PUT instead. Updates asset group selectors.

    Args:
        asset_group_id (int):
        prefer (Union[Unset, int]):  Default: 0.
        body (List['ModelAssetGroupSelectorSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]
    """

    kwargs = _get_kwargs(
        asset_group_id=asset_group_id,
        body=body,
        prefer=prefer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["ModelAssetGroupSelectorSpec"],
    prefer: Union[Unset, int] = 0,
) -> Optional[Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]]:
    """Update asset group selectors

     DEPRECATED use PUT instead. Updates asset group selectors.

    Args:
        asset_group_id (int):
        prefer (Union[Unset, int]):  Default: 0.
        body (List['ModelAssetGroupSelectorSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAssetGroupSelectorsDeprecatedResponse201]
    """

    return (
        await asyncio_detailed(
            asset_group_id=asset_group_id,
            client=client,
            body=body,
            prefer=prefer,
        )
    ).parsed
