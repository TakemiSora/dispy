from datetime import datetime
from typing import Self

from ..payloads.embed import (
    EmbedAuthorPayload,
    EmbedFieldPayload,
    EmbedFooterPayload,
    EmbedMediaPayload,
    EmbedImagePayload,
    EmbedPayload,
    EmbedProviderPayload,
    EmbedVideoPayload
)
from ..enums.embed import (
    EmbedType
)
from ..flags import (
    EmbedMediaFlags,
    EmbedFlags
)
from ..utils import siso, scls

__all__ = (
    "EmbedFooter",
    "EmbedImage",
    "EmbedAuthor",
    "EmbedField",
    "Embed",
)

class EmbedFooter:
    __slots__ = (
        "text",
        "icon_url",
        "proxy_icon_url"
    )
    
    def __init__(self, data: EmbedFooterPayload):
        self.text = data["text"]
        self.icon_url = data.get("icon_url")
        self.proxy_icon_url = data.get("proxy_icon_url")

    def _to_dict(self) -> EmbedFooterPayload:
        footer = EmbedFooterPayload(text=self.text)
        if self.icon_url is not None: footer["icon_url"] = self.icon_url
        return footer

    @classmethod
    def new(
        cls, *,
        text: str,
        icon_url: str | None = None
    ) -> Self:
        footer = cls(EmbedFooterPayload(text=text))
        footer.icon_url = icon_url
        return footer

class EmbedMedia:
    __slots__ = (
        "proxy_url",
        "height",
        "width",
        "content_type",
        "placeholder",
        "placeholder_version",
        "description",
        "flags"
    )

    def __init__(self, data: EmbedMediaPayload):
        self.proxy_url = data.get("proxy_url")
        self.height = data.get("height")
        self.width = data.get("width")
        self.content_type = data.get("content_type")
        self.placeholder = data.get("placeholder")
        self.placeholder_version = data.get("placeholder_version")
        self.description = data.get("description")
        self.flags = EmbedMediaFlags(data.get("flags", 0))

class EmbedImage(EmbedMedia):
    __slots__ = (
        "url",
    )

    def __init__(self, data: EmbedImagePayload):
        super().__init__(data)
        self.url = data["url"]

    def _to_dict(self) -> EmbedImagePayload:
        return EmbedImagePayload(url=self.url)

    @classmethod
    def new(cls, *, url: str) -> Self:
        return cls(EmbedImagePayload(url=url))

class EmbedVideo(EmbedMedia):
    __slots__ = (
        "url",
    )

    def __init__(self, data: EmbedVideoPayload):
        super().__init__(data)
        self.url = data.get("url")

class EmbedProvider:
    __slots__ = (
        "name",
        "url"
    )

    def __init__(self, data: EmbedProviderPayload):
        self.name = data.get("name")
        self.url = data.get("url")

class EmbedAuthor:
    __slots__ = (
        "name",
        "url",
        "icon_url",
        "proxy_icon_url"
    )

    def __init__(self, data: EmbedAuthorPayload):
        self.name = data["name"]
        self.url = data.get("url")
        self.icon_url = data.get("icon_url")
        self.proxy_icon_url = data.get("proxy_icon_url")

    @classmethod
    def new(
        cls, *,
        name: str,
        url: str | None = None,
        icon_url: str | None,
    ) -> Self:
        author = cls(EmbedAuthorPayload(name=name))
        author.url = url
        author.icon_url= icon_url
        return author

class EmbedField:
    __slots__ = (
        "name",
        "value",
        "inline"
    )

    def __init__(self, data: EmbedFieldPayload):
        self.name = data["name"]
        self.value = data["value"]
        self.inline = data.get("inline", False)

    def _to_dict(self) -> EmbedFieldPayload:
        return EmbedFieldPayload(
            name=self.name,
            value=self.value,
            inline=self.inline
        )

    @classmethod
    def new(
        cls, *,
        name: str,
        value: str,
        inline: bool = False
    ) -> Self:
        return cls(EmbedFieldPayload(
            name=name,
            value=value,
            inline=inline
        ))

class Embed:
    __slots__ = (
        "title",
        "type",
        "description",
        "url",
        "timestamp",
        "color",
        "footer",
        "image",
        "thumbnail",
        "video",
        "provider",
        "author",
        "fields",
        "flags"
    )
    
    def __init__(self, data: EmbedPayload):
        self.title = data.get("title")
        self.type = scls(EmbedType, data.get("type"))
        self.description = data.get("description")
        self.url = data.get("url")
        self.timestamp = siso(data.get("timestamp"))
        self.color = data.get("color")
        self.footer = scls(EmbedFooter, data.get("footer"))
        self.image = scls(EmbedImage, data.get("image"))
        self.thumbnail = scls(EmbedImage, data.get("thumbnail"))
        self.video = scls(EmbedVideo, data.get("video"))
        self.provider = scls(EmbedProvider, data.get("provider"))
        self.author = scls(EmbedAuthor, data.get("author"))
        self.fields = [EmbedField(f) for f in data.get("fields", [])]
        self.flags = EmbedFlags(data.get("flags", 0))

    def _to_dict(self) -> EmbedPayload:
        embed = EmbedPayload()
        if self.title is not None: embed["title"] = self.title
        if self.type is not None: embed["type"] = self.type.value
        if self.description is not None: embed["description"] = self.description
        if self.timestamp is not None: embed["timestamp"] = self.timestamp.isoformat()
        if self.color is not None: embed["color"] = self.color
        if self.footer is not None: embed["footer"] = self.footer._to_dict()
        if self.image is not None: embed["image"] = self.image._to_dict()
        if self.thumbnail is not None: embed["thumbnail"] = self.thumbnail._to_dict()
        if self.fields is not None: embed["fields"] = [f._to_dict() for f in self.fields]
        return embed

    @classmethod
    def new(
        cls, *,
        title: str | None = None,
        description: str | None = None,
        timestamp: datetime | None = None,
        color: int | None = None,
        footer: EmbedFooter | None = None,
        image: EmbedImage | None = None,
        thumbnail: EmbedImage | None = None,
        author: EmbedAuthor | None = None,
        fields: list[EmbedField] | None = None
    ) -> Self:
        embed = cls(EmbedPayload(type=EmbedType.rich))
        embed.title = title
        embed.description = description
        embed.timestamp = timestamp
        embed.color = color
        embed.footer = footer
        embed.image = image
        embed.thumbnail = thumbnail
        embed.author = author
        embed.fields = fields
        return embed