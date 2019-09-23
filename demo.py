
class person(object):
    def __init__(self):
        print ("__init__")
    def __new__(cls, *args, **kwargs):
        print ("__new__")
        return object.__new__(cls, *args, **kwargs)

p = person()