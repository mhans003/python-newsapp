from flask import session, redirect
# Import wraps to use as a decorator function to protect private routes.
from functools import wraps

def login_required(func):
    # Use @wraps to maintain original function name when creating wrapped function.
    @wraps(func)
    # Capture all arguments in wrapped_function.
    def wrapped_function(*args, **kwargs):
        # If currently logged in, call original function with original arguments.
        if session.get('loggedIn') == True:
            return func(*args, **kwargs)
        # Otherwise, redirect to login page.
        return redirect('/login')
    return wrapped_function