def test(func, args_expects):
    correct = True
    for args, expect in args_expects:
        if type(args) in (tuple, list):
            result = func(*args)
        else:
            result = func(args)
        if expect != result:
            correct = False
            print("When input is {}, {} is expected but got {}".format(args, expect, result))
    if correct:
        print('OK!')
