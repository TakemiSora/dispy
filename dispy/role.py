from typing import Literal
from .snowflake import Snowflake
from .http import State
from .asset import Asset
from .flags import RoleFlags

class RoleColors:
    def __init__(self, data: dict[str, int | None]):
        self.primary: int = data["primary_color"]
        self.secondary = data.get("secondary_color")
        self.tertiary = data.get("tertiary_color")

class Role(Snowflake):
    def __init__(self, state: State, data: dict[str, Any]):
        self._state = state
            
        super().__init__(int(data["id"]))
        self.name: str = data["name"]
        self.colors = RoleColors(data["colors"])
        self.hoist: bool = data["host"]
        self.icon = Asset._from_role_icon(state, self.id, data.get("icon"))
        self.emoj: str | None = data.get("unicode_emoji")
        self.position: int = data["position"]
        #implement permissions later
        self.managed: bool = data["managed"]
        self.mentionable: bool = data["mentionable"]
        #implement roletags later
        self.flags = RoleFlags(data["flags"])