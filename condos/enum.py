from enum import Enum


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class Types(ChoicesEnum):
    BOTH = 'Both'
    LEASE = 'Lease'
    RENT = 'Rent'
