import collections
import copy
import inspect


def test(funcs, args_expects, copy_parameters=True):
    correct = True
    if not isinstance(funcs, collections.Iterable):
        funcs = [funcs]
    for func in funcs:
        for args, expect in args_expects:
            if copy_parameters:
                args = copy.deepcopy(args)
            if type(args) in (list, tuple) and len(args) > 1 and len(args) == len(inspect.getargspec(func).args) - 1:
                result = func(*args)
            elif args:
                result = func(args)
            else:
                result = func()
            if expect != result:
                correct = False
                print("When calling {} with input '{}', '{}' is expected but got '{}'".format(func, args, expect, result))
    if correct:
        print('OK!')
