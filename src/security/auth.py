from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Dummy authentication
        return f(*args, **kwargs)
    return decorated