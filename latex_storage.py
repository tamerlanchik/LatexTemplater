import os
from decimal import Decimal


class Storage(object):
    _map = {}

    def _put(self, key, value):
        self._map[key] = value

    def put(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, float):
                temp = value - int(value)
                value = int(value) + Decimal('{:g}'.format(Decimal('{:.{p}g}'.format(temp, p=2))))
            self._put(key, str(value))

    def pop(self, key):
        return self._map.pop(key, None)

    def export(self, filename):
        assert filename != ''
        with open(filename, 'w', encoding='utf8') as file:
            import json
            json.dump(self._map, file, indent=4, ensure_ascii=False)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
        return cls.instance
