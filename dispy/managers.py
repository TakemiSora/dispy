from .objects.user import User
from .objects.message import Message
from .objects.guild import Guild
from .objects.channel import GuildChannel, PrivateChannel, ThreadChannel, parse_channel_payload
from .http import HTTPClient, Path
from .cache import CacheStorage

class BaseManager:
    __slots__ = (
        "_http",
        "_cache_storage"
    )

    def __init__(self, client: HTTPClient, cache: CacheStorage):
        self._http = client
        self._cache_storage = cache

class Users(BaseManager):
    __slots__ = ()

    def get(self, user_id: int) -> User | None:
        return self._cache_storage.get_user(user_id)

    async def fetch(self, user_id: int) -> User:
        return self._cache_storage.update_users(
            User(await self._http.request(
                Path(
                    "GET",
                    "users/{user_id}",
                    user_id=user_id
            )))
        )

    async def get_or_fetch(self, user_id: int) -> User:
        return self.get(user_id) or await self.fetch(user_id)

class Messages(BaseManager):
    __slots__ = ()

    def get(self, message_id: int) -> Message | None:
        return self._cache_storage.get_message(message_id)

    async def fetch(self, channel_id: int, message_id: int) -> Message:
        return self._cache_storage.update_messages(
            Message(await self._http.request(
                Path(
                    "GET",
                    "channels/{channel_id}/messages/{message_id}",
                    channel_id=channel_id,
                    message_id=message_id
            )))
        )

    async def get_or_fetch(self, channel_id: int, message_id: int) -> Message:
        return self.get(message_id) or await self.fetch(channel_id, message_id)

class Channels(BaseManager):
    __slots__ = ()

    def get(self, channel_id: int) -> ThreadChannel | GuildChannel | PrivateChannel | None:
        return self._cache_storage.get_channel(channel_id)

    async def fetch(self, channel_id: int) -> ThreadChannel | GuildChannel | PrivateChannel:
        return self._cache_storage.update_channels(
            parse_channel_payload(await self._http.request(
                Path(
                    "GET",
                    "channels/{channel_id}",
                    channel_id=channel_id
            )))
        )

    async def get_or_fetch(self, channel_id: int) -> ThreadChannel | GuildChannel | PrivateChannel:
        return self.get(channel_id) or await self.fetch(channel_id)


class Guilds(BaseManager):
    __slots__ = ()

    def get(self, guild_id: int) -> Guild | None:
        return self._cache_storage.get_guild(guild_id)

    async def fetch(self, guild_id: int) -> Guild:
        return self._cache_storage.update_guilds(
            Guild(await self._http.request(
                Path(
                    "GET",
                    "guilds/{guild_id}",
                    guild_id=guild_id
            )))
        )
    
    async def get_or_fetch(self, guild_id: int) -> Guild:
        return self.get(guild_id) or await self.fetch(guild_id)