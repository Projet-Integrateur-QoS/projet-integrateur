from json import JSONEncoder
from collections import deque

class CustomEncoder(JSONEncoder):
    def default(self, obj):
       if isinstance(obj, deque):
          return list(obj)
       return JSONEncoder.default(self, obj)
