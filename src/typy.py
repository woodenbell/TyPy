import inspect


class TypeException(Exception):
    def __init__(self, msg, t, expected_t):
        super().__init__(msg)
        self.t = t
        self.expected_t = expected_t


class InvalidTypeCheckException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def typed(f):
    def do_typecheck(v, t, v_name):
        if type(t) is type:
            if not issubclass(type(v), t):
                raise TypeException("Expected %s to be of type %s, but type %s received" %
                                    (v_name, t, type(v)), type(v), t)
        elif type(t) is tuple:
            if not len(v) == len(t):
                raise TypeException("Expected %s to be of a tuple of size %s, but size %s received" %
                                    (v_name, len(t), len(v)), None, None)
            else:
                for i, val in enumerate(v):
                    do_typecheck(val, t[i], v_name)

        elif type(t) is set:
            if not type(v) in t:
                raise TypeException("Expected %s to be of types %s, but type %s received" %
                                    (v_name, list(t), type(v)), type(v), t)
        elif type(t) is list:
            if len(t) != 2:
                raise InvalidTypeCheckException("Invalid structure typecheck %s, only 2 elements are allowed" % t)

            if not issubclass(type(v), t[0]):
                raise TypeException("Expected data structure %s to be of type %s, but type %s received" %
                                    (v_name, t[0], type(v)), type(v), t[0])
            else:
                if type(v) == dict:
                    iterable = v.values()
                elif type(v) == set or type(v) == list or type(v) == tuple:
                    iterable = list(v)
                else:
                    raise InvalidTypeCheckException("Invalid data structure for typechecking: %s" % type(v))

                for i in iterable:
                    do_typecheck(i, t[1], v_name)

        else:
            raise InvalidTypeCheckException("Invalid type: %s" % t)

    annos = f.__annotations__




    

    def wrapper(*args, **kargs):
        args_dict = dict(zip(inspect.getfullargspec(f)[0], args))
        for k, v in args_dict.items():
            if k in annos.keys():
                do_typecheck(v, annos[k], k)
        for k2, v2 in kargs.items():
            if k2 in annos.keys():
                do_typecheck(v2, annos[k2], k2)

        f_ret = f(*args, **kargs)

        if "return" in annos.keys():
            do_typecheck(f_ret, annos["return"], "return")
        return f_ret

    return wrapper
