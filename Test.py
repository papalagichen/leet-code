import copy
import inspect


def test(func, args_expects):
    correct = True
    for args, expect in args_expects:
        if type(args) in (list, tuple) and len(args) == len(inspect.getargspec(func).args) - 1:
            result = func(*copy.deepcopy(args))
        else:
            result = func(copy.deepcopy(args))
        if expect != result:
            correct = False
            print("When input is '{}', '{}' is expected but got '{}'".format(args, expect, result))
    if correct:
        print('OK!')
