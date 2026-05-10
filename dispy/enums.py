from enum import IntEnum

class NitroType(IntEnum):
    NONE = 0
    CLASSIC = 1
    NITRO = 2
    BASIC = 3

class GuildVerificationLevel(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4
    
class GuildNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1
    
class GuildExplicitContentLevel(IntEnum):
    DISABLED = 0
    MEMBER_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2