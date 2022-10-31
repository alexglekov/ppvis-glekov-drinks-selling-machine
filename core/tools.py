import importlib


def get_class(cls_tuple):
    module = importlib.import_module(cls_tuple[0])
    val = getattr(module, cls_tuple[1])
    return val
