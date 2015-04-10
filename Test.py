def test(expect, got):
    if expect == got:
        print("OK")
    else:
        print("Expect {} but got {}".format(expect, got))
