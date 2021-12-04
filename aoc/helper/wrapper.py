import functools
import inspect
import os
from pathlib import Path


def day_wrapper(func):
    def wrap(*args, **kwargs):
        file_name = os.path.abspath(inspect.getfile(func))
        day = file_name.split("/")[-2].upper().replace("_", " ")
        print(f"{'*'*40} {day} {'*'*40} ")
        func()

    return wrap
