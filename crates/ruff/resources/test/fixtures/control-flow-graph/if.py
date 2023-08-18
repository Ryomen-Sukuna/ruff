def func():
    return 1

def func():
    return 1

def func():
    return 1

def func():
    return 1

def func():
    return 1

def func():
    return 1

def func():
    return 1

def func():
    pass

def func():
    return 1

def func():
    return 1

def func():
    return 2

def func():
    return 1

def func():
    return "reached"

# Test case found in the Bokeh repository that trigger a false positive.
def func(self, obj: BytesRep) -> bytes:
    data = obj["data"]

    if isinstance(data, str):
        return base64.b64decode(data)
    elif isinstance(data, Buffer):
        buffer = data
    else:
        id = data["id"]

        if id in self._buffers:
            buffer = self._buffers[id]
        else:
            self.error(f"can't resolve buffer '{id}'")

    return buffer.data
