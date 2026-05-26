from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any
from .utils import scls

from .payloads.channel import (
    PrivateChannelPayload,
    GuildChannelPayload,
    ThreadCreatePayload,
    ThreadDeletePayload,
    ThreadPayload
)
from .objects.channel import (
    ThreadChannel,
    ThreadMember,
    parse_channel_payload
)
from .enums.channel import ChannelType
from .payloads.guild import (
    GuildPayload,
    UnavailableGuildPayload,
)
from .objects.guild import (
    Guild,
    UnavailableGuild,
    parse_guild_payload
)

if TYPE_CHECKING:
    from .bot import Bot

class EventDispatcher:
    __slots__ = (
        "_dispatch_handlers",
        "bot"
    )

    def __init__(self, bot: Bot):
        self.bot = bot
        self._dispatch_handlers = {
            # GUILDS 
                "GUILD_CREATE": self._handle_guild_create,
                "GUILD_UPDATE": self._handle_guild_update,
                "GUILD_DELETE": self._handle_guild_delete,
                "CHANNEL_CREATE": self._handle_channel_create,
                "CHANNEL_UPDATE": self._handle_channel_update,
                "CHANNEL_DELETE": self._handle_channel_delete,
                "THREAD_CREATE": self._handle_thread_create,
                "THREAD_UPDATE": self._handle_thread_update,
                "THREAD_DELETE": self._handle_thread_delete,
        }

    async def _dispatch(self, key: str, *args: Any):
        for f in self.bot._listeners.get(key, []):
            asyncio.create_task(f(*args))
            
    async def _handle_guild_create(self, data: GuildPayload | UnavailableGuildPayload):
        guild = self.bot.storage.update_guilds(g) if isinstance((g := parse_guild_payload(data)), Guild) else g
        await self._dispatch("on_guild_create", guild)
        
    async def _handle_guild_update(self, data: GuildPayload):
        guild = self.bot.storage.update_guilds(Guild(data))
        await self._dispatch("on_guild_update", guild)
    
    async def _handle_guild_delete(self, data: UnavailableGuildPayload):
        guild = UnavailableGuild(data)
        kicked = not guild.unavailable
        await self._dispatch("on_guild_delete", guild, kicked)

    async def _handle_channel_create(self, data: GuildChannelPayload | PrivateChannelPayload):
        channel = self.bot.storage.update_channels(parse_channel_payload(data))
        await self._dispatch("on_channel_create", channel)

    async def _handle_channel_update(self, data: GuildChannelPayload | PrivateChannelPayload):
        channel = self.bot.storage.update_channels(parse_channel_payload(data))
        await self._dispatch("on_channel_update", channel)

    async def _handle_channel_delete(self, data: GuildChannelPayload | PrivateChannelPayload):
        channel = self.bot.storage.remove_channel(int(data["id"]))
        await self._dispatch("on_channel_delete", channel or parse_channel_payload(data))

    async def _handle_thread_create(self, data: ThreadCreatePayload):
        newly_created = data.get("newly_created", False)
        thread_member = scls(ThreadMember, data.get("member"))
        channel = self.bot.storage.update_channels(ThreadChannel(data))
        await self._dispatch("on_thread_create", channel, newly_created, thread_member)

    async def _handle_thread_update(self, data: ThreadPayload):
        channel = self.bot.storage.update_channels(ThreadChannel(data))
        await self._dispatch("on_thread_update", channel)

    async def _handle_thread_delete(self, data: ThreadDeletePayload):
        id = int(data["id"])
        guild_id = int(data["guild_id"])
        parent_id = int(data["parent_id"])
        type = ChannelType(data["type"])
        self.bot.storage.remove_channel(id)
        await self._dispatch("on_thread_delete", id, guild_id, parent_id, type)