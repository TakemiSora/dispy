from typing import Any
from .http import State
from .asset import Asset
from .enums import GuildVerificationLevel, GuildNotificationLevel, GuildExplicitContentLevel

class Guild:
    def __init__(self, state: State, data: dict[str, Any]):
        self._state = state

        self.id = int(data["id"])
        self.name: str = data["name"]
        self.icon = Asset._from_guild_avatar(state, self.id, data.get("icon"))
        self.splash = Asset._from_guild_splash(state, self.id, data.get("splash")) 
        self.discovery_splash = Asset._from_guild_discovery_splash(state, self.id, data.get("discovery_splash"))
        self.owner_id = int(data["owner_id"])
        self.afk_channel_id = int(data["afk_channel_id"]) if data.get("afk_channel_id") else None
        self.afk_timeout = data["afk_timeout"]
        self.verification_level = GuildVerificationLevel(data["verification_level"])
        self.notification_level = GuildNotificationLevel(data["default_message_notifications"])
        self.explicit_level = GuildExplicitContentLevel(data["explicit_content_filter"])
        #to implement everything here after later

    def __str__(self) -> str:
        return self.name
    
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.sku_id == obj.sku_id
        return NotImplemented
    
    def __hash__(self) -> int:
        return self.sku_id