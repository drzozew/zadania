import numpy as np
def gen_fun():
    start = 2
    end = 6
    step = 0.5

    ls = []
    for i in np.arange(start, end, step):
        print(i, end=' ')
        print(type(i))
        ls.append(i)

    print(ls)

gen_fun()
