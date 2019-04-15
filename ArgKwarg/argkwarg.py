# Design of the ALU in python using *arg and **kwargs
def prints(func):
    def f(*args, **kwargs):
        rv = func(*args, **kwargs)
        for key, value in kwargs.items():
            print("{}'s result:{}".format(value,rv))
        return rv
    return f

@prints
def ALU(*args, **kwargs):
    for key, values in kwargs.items():
        if (values == 'add'):
            try:
                rv = args[0] + args[1]
                return rv
            except:
                raise AssertionError('Wrong number of arguments')
        elif (values == 'sub'):
            try:
                rv = args[0] - args[1]
                return rv
            except:
                raise AssertionError('Wrong number of arguments')
        elif (values == 'div'):
            try:
                rv = args[0] / args[1]
                return rv
            except:
                raise AssertionError('Wrong number of arguments')
        elif (values == 'mul'):
            try:
                rv = args[0] * args[1]
                return rv
            except:
                raise AssertionError('Wrong number of arguments')
        elif (values == 'abs'):
            try:
                rv = abs(args[0])
                return rv
            except:
                raise AssertionError('Wrong number of arguments')
        
a = ALU(8, 10, ope='add')
a = ALU(10, 8, ope='sub')
a = ALU(8, 4, ope='div')
a = ALU(4, 2, ope='mul')
a = ALU(-8, ope='abs')