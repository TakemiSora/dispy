class Snowflake:
    def __init__(self, snowflake: int):
        self.id = snowflake

    def __eq__(self, object: object) -> bool:
        if isinstance(object, self.__class__):
            return self.id == object.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)