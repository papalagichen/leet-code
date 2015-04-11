import copy
import inspect


def test(func, args_expects, copy_parameters=True):
    correct = True
    for args, expect in args_expects:
        if copy_parameters:
            args = copy.deepcopy(args)
        if type(args) in (list, tuple) and len(args) == len(inspect.getargspec(func).args) - 1:
            result = func(*args)
        else:
            result = func(args)
        if expect != result:
            correct = False
            print("When input is '{}', '{}' is expected but got '{}'".format(args, expect, result))
    if correct:
        print('OK!')
