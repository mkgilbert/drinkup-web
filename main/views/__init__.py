import os
import re
import types
import importlib

view_names = []

view_dir = os.path.dirname(__file__)
if view_dir == '':
    view_dir = '.'

for filename in os.listdir(view_dir):
    if not re.match(r"^.*.py$", filename) or filename == "__init__.py":
        continue
    view_module = importlib.import_module(__name__ + "." + filename[:-3])
    for view_name in dir(view_module):
        view_function = getattr(view_module, view_name)
        if not isinstance(view_function, (type, types.FunctionType)):
            continue
        globals()[view_name] = view_function
        view_names.append(view_name)


__all__ = view_names
