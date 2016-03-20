import os
import re
import importlib

form_names = []

form_dir = os.path.dirname(__file__)
if form_dir == '':
    form_dir = '.'

for filename in os.listdir(form_dir):
    if not re.match(r"^.*.py$", filename) or filename == "__init__.py":
        continue
    form_module = importlib.import_module(__name__ + "." + filename[:-3])
    for form_name in dir(form_module):
        form_class = getattr(form_module, form_name)
        if not isinstance(form_class, type):
            continue
        globals()[form_name] = form_class
        form_names.append(form_name)

__all__ = form_names