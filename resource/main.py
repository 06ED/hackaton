import inspect
import sys

from flask_restful import Api

import resource.resources


def register(api: Api):
    classes = inspect.getmembers(sys.modules[resource.resources.__name__], inspect.isclass)

    for class_info in classes:
        name, cls = class_info
        api.add_resource(cls, f"/api/{cls.address}/")


