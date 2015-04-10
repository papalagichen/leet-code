def test(func, args_expects):
    for args, expect in args_expects:
        if type(args) in (tuple, list):
            result = func(*args)
        else:
            result = func(args)
        if expect == result:
            print("OK")
        else:
            print("Expect {} but got {}".format(expect, result))
