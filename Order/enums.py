import enum


class Status(enum.Enum):
    created = 1
    pending = 2
    failed = 3
    placed = 4
