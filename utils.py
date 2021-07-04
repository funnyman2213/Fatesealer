import asyncio

class Cacheable:
    def __init__(self, co):
        self.co = co
        self.done = False
        self.result = None
        self.lock = asyncio.Lock()

    def __await__(self):
        with (yield from self.lock):
            if self.done:
                return self.result
            self.result = yield from self.co.__await__()
            self.done = True
            return self.result

def cacheable(f):
    def wrapped(*args, **kwargs):
        r = f(*args, **kwargs)
        return Cacheable(r)
    return wrapped