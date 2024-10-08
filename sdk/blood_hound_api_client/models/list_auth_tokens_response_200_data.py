from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_auth_token import ModelAuthToken


T = TypeVar("T", bound="ListAuthTokensResponse200Data")


@_attrs_define
class ListAuthTokensResponse200Data:
    """
    Attributes:
        tokens (Union[Unset, List['ModelAuthToken']]):
    """

    tokens: Union[Unset, List["ModelAuthToken"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = []
            for tokens_item_data in self.tokens:
                tokens_item = tokens_item_data.to_dict()
                tokens.append(tokens_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_auth_token import ModelAuthToken

        d = src_dict.copy()
        tokens = []
        _tokens = d.pop("tokens", UNSET)
        for tokens_item_data in _tokens or []:
            tokens_item = ModelAuthToken.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        list_auth_tokens_response_200_data = cls(
            tokens=tokens,
        )

        list_auth_tokens_response_200_data.additional_properties = d
        return list_auth_tokens_response_200_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
