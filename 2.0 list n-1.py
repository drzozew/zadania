def n_list(n, ls_in):
    n_ls =[x for x in range(1, n+1)]

    not_in_ls = []

    for i in n_ls:
        if i not in ls_in:
            not_in_ls.append(i)

    print(not_in_ls)


ls_in = [2,3,7,4,9,10]
n = 100

n_list(n, ls_in)