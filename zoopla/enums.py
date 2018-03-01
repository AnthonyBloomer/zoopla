from enum import Enum


class AreaType(Enum):
    STREETS = 'streets'
    POSTCODES = 'postcodes'
    OUTCODES = 'outcodes'
    AREAS = 'areas'
    TOWNS = 'towns'
    COUNTIES = 'counties'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<AreaType: %s>" % self


class OutputType(Enum):
    STREET = 'street'
    POSTCODE = 'postcode'
    OUTCODE = 'outcode'
    AREA = 'area'
    TOWN = 'town'
    COUNTY = 'county'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<OutputType: %s>" % self
