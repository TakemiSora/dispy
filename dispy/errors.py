from typing import Any

__all__ = (
    "HTTPException",
    "GatewayError",
    "NotFound",
    "Forbidden",
    "Unauthorized",
    "ImproperToken",
    "UnknownChannelType",
    "InteractionResponded",
    "InteractionNotResponded"
)

class HTTPException(Exception):
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message
        super().__init__(f"HTTP {status}: {message}")

class GatewayError(Exception):
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message
        super().__init__(f"Gateway Closed with {status}: {message}")

class NotFound(HTTPException):
    pass

class Forbidden(HTTPException):
    pass

class Unauthorized(HTTPException):
    pass

class ImproperToken(HTTPException):
    pass

class UnknownChannelType(Exception):
    pass
        
class UnknownInteractionType(Exception):
    pass

class InteractionResponded(Exception):
    pass

class InteractionNotResponded(Exception):
    pass

class RateLimitedRetry(Exception):
    def __init__(self, data: dict[str, Any], retry_after: float, limit_scope: str | None, bucket_id: str | None):
        self.data = data
        self.retry_after = retry_after
        self.limit_scope = limit_scope
        self.bucket_id = bucket_id