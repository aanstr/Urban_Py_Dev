import inspect
import math


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    obj_module = inspect.getmodule(obj) if inspect.getmodule(obj) else 'Unknown'
    additional_info = getattr(obj, '__doc__')

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'additional_info': additional_info
    }


class NewClass:
    def __init__(self, arg):
        self.arg = arg

    def new_meth(self):
        return math.sqrt(self.arg)


obj = NewClass(math.pi)

number_info = introspection_info(42)
print(number_info)

new_obj_info = introspection_info(obj)
print(new_obj_info)
