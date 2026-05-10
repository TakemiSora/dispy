import aiohttp
import asyncio
from .http import State
from .managers import Users
from .gateway import GatewayClient
from .flags import IntentFlags

class Bot:
    def __init__(
        self,
        token: str,
        intents: IntentFlags
    ):
        self.token = token
        self._state = State()
        self._gateway_client = GatewayClient(token, intents)
        self.users = Users(self._state)

    def run(self) -> None:
        asyncio.run(self.start())

    async def start(self) -> None:
        try:
            self._state.session = aiohttp.ClientSession(
                "https://discord.com/api/v10/",
                headers={
                    "Authorization": f"Bot {self.token}"
                }
            )
            await self._gateway_client.connect()
            await self._gateway_client.wait_until_closed()
        finally:
            await self.stop()

    async def stop(self) -> None:
        await self._gateway_client.close()
        await self._state.session.close()