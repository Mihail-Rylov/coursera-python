from json import dumps
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = dumps(func(*args, **kwargs))
        return result
    return wrapped

@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data())  # вернёт '{"data": 42}'