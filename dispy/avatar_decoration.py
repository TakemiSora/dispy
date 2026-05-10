from __future__ import annotations
from typing import Any
from .asset import Asset
from .http import State
from .snowflake import Snowflake

class AvatarDecoration(Snowflake):
    def __init__(self, state: State, data: dict[str, Any]):
        self._state = state

        super().__init__(int(data["sku_id"]))
        self.asset = Asset._from_user_avatar_decoration(state, data["asset"])

    @classmethod
    def _from_dict(cls, state: State, data: dict[str, Any] | None) -> AvatarDecoration | None:
        if data is not None:
            return cls(state, data)
        return None
