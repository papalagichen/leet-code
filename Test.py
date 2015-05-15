import collections
import copy
import inspect
import types


def test(funcs, args_expects, copy_parameters=True):
    correct = True
    if not isinstance(funcs, collections.Iterable):
        funcs = [funcs]
    for func in funcs:
        for args, expect in args_expects:
            if copy_parameters:
                args = copy.deepcopy(args)
            spec_args = inspect.getargspec(func).args
            spec_args_count = len(spec_args) - (1 if len(spec_args) > 0 and spec_args[0] == 'self' else 0)
            if type(args) in (list, tuple) and len(args) > 1 and len(args) == spec_args_count:
                result = func(*args)
            elif args is None and len(inspect.getargspec(func).args) == 1:
                result = func()
            else:
                result = func(args)
            if isinstance(result, types.GeneratorType):
                result = list(result)
            if expect != result:
                correct = False
                print("When calling {} with input '{}', '{}' is expected but got '{}'".format(
                    func, args, expect, result))
    if correct:
        print('OK!')


def equal(expect, given):
    if expect == given:
        print('OK!')
    else:
        print("Expect: '{}' Given: '{}'".format(expect, given))
