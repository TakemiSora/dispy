from __future__ import annotations
from typing import NotRequired, Required, TypedDict, Literal
from ._types import Snowflake

class CommandChoicePayload(TypedDict):
    name: str
    name_localizations: NotRequired[dict[str, str] | None]
    value: str | int | float

class CommandOptionPayload(TypedDict, total=False):
    type: Required[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    name: Required[str]
    name_localizations: dict[str, str] | None
    description: Required[str]
    description_localizations: dict[str, str] | None
    required: bool
    choices: list[CommandChoicePayload]
    options: list[CommandOptionPayload]
    channel_types: Literal[0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16]
    min_value: int | float
    max_value: int | float
    min_length: int
    max_length: int
    autocomplete: bool

class ApplicationCommandPayload(TypedDict):
    id: Required[Snowflake]
    type: Literal[1, 2, 3, 4]
    application_id: Required[Snowflake]
    guild_id: Snowflake
    name: Required[str]
    name_localizations: dict[str, str] | None
    description: Required[str]
    description_localizations: dict[str, str] | None