def satmul(seq):
    sumb = 0
    for i in seq:
        for j in seq:
            if i == j:
                continue
            for k in seq:
                if j != k:
                    x = ((i * 10) + j) * k
                    y = list(f"{i}{j}{k}")
                    if x < 100 and ((str(x)[0] not in y) and (str(x)[1] not in y)):
                        # print(i, j, k, x)
                        pre = f"{i}{j}{k}"
                        e = x
                        a = satadd(seq, pre, e)
                        if a == None:
                            continue
                        else:
                            pre = f"{i}{j}{k}{str(x)[0]}{str(x)[1]}"
                            if (
                                str(a[0]) in pre
                                or str(a[1]) in pre
                                or (str(0) in list(str(a[2])))
                            ):
                                continue
                            return f"{pre[:2]}*{pre[2]}={x}\t{x}+{str(a[0])+str(a[1])} = {a[2]}"
                    else:
                        continue
                else:
                    pass


def satadd(seq, pre, e):
    for i in seq:
        for j in seq:
            if i == j:
                continue
            if (str(i) not in pre) and (str(j) not in pre):
                # print(i, j)
                res = ((i * 10) + j) + e
                pres = f"{pre[0]}{pre[1]}{pre[2]}{str(e)[0]}{str(e)[1]}"
                y = list(f"{i}{j}" + pres)

                if res < 100:
                    # print(y)
                    lex = len(str(res))
                    con2 = [None] * lex
                    stres = [None] * lex
                    for f in range(lex):
                        con2[f] = int(bool(str(res)[f] not in y))
                        stres[f] = int(str(res)[f])
                    if 0 not in con2 and len(set(stres)) == lex:
                        if res == None:
                            return None
                        else:
                            return [i, j, res]
                    else:
                        continue
                else:
                    continue
            else:
                continue


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(satmul(l))

