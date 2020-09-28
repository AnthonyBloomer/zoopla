from marshmallow.fields import String


class StrippedString(String):
    def deserialize(self, value, attr=None, data=None):
        result = super(StrippedString, self).deserialize(value, attr, data)
        return result.strip()
