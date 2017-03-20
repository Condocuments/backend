from enum import Enum


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class Types(ChoicesEnum):
    BOTH = 'Both'
    LEASE = 'Lease'
    RENT = 'Rent'


class ContentType(ChoicesEnum):
    CONDO = 'Condo'
    USER = 'User'


class PropertyType(ChoicesEnum):
    RENT = 'For rent'
    SALE = 'For sale'
