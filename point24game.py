def main():
    fir = input('the first number:')
    sec = input('the second number:')
    thi = input('the third number:')
    fou = input('the fourth number:')
    num = [fir, sec, thi, fou]
    sign = ['+', '-', '*', '/']
    xuhao = [0, 1, 2, 3]
    printed = set()
    if fir.isdigit() and sec.isdigit() and thi.isdigit() and fou.isdigit():
        for a in xuhao:
            for b in xuhao:
                if b == a:
                    continue
                for c in xuhao:
                    if c == a or c == b:
                        continue
                    for d in xuhao:
                        if d == a or d == b or d == c:
                            continue
                        for e in range(4):
                            for f in range(4):
                                for g in range(4):
                                    yi = num[a] + sign[e] + num[b] + sign[f] + num[c] + sign[g] + num[d]
                                    er = '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + num[c] + sign[g] + num[d]
                                    san = '(' + num[a] + sign[e] + num[b] + sign[f] + num[c] + ')' + sign[g] + num[d]
                                    si = '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + '(' + num[c] + sign[g] + num[
                                        d] + ')'
                                    try:
                                        result1 = eval(yi)
                                    except ZeroDivisionError:
                                        result1 = 0
                                    try:
                                        result2 = eval(er)
                                    except ZeroDivisionError:
                                        result2 = 0
                                    try:
                                        result3 = eval(san)
                                    except ZeroDivisionError:
                                        result3 = 0
                                    try:
                                        result4 = eval(si)
                                    except ZeroDivisionError:
                                        result4 = 0
                                    if result1 == 24:
                                        if yi not in printed:
                                            print(yi, '=24')
                                            printed.add(num[a] + sign[e] + num[b] + sign[f] + num[c] + sign[g] + num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + num[c] + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + sign[f] + num[c] + ')' + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + '(' + num[c] + sign[
                                                    g] +
                                                num[
                                                    d] + ')')
                                    if result2 == 24:
                                        if er not in printed:
                                            print(er, '=24')
                                            printed.add(num[a] + sign[e] + num[b] + sign[f] + num[c] + sign[g] + num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + num[c] + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + sign[f] + num[c] + ')' + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + '(' + num[c] + sign[
                                                    g] +
                                                num[
                                                    d] + ')')
                                    if result3 == 24:
                                        if san not in printed:
                                            print(san, '=24')
                                            printed.add(num[a] + sign[e] + num[b] + sign[f] + num[c] + sign[g] + num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + num[c] + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + sign[f] + num[c] + ')' + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + '(' + num[c] + sign[
                                                    g] +
                                                num[
                                                    d] + ')')
                                    if result4 == 24:
                                        if si not in printed:
                                            print(si, '=24')
                                            printed.add(num[a] + sign[e] + num[b] + sign[f] + num[c] + sign[g] + num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + num[c] + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + sign[f] + num[c] + ')' + sign[g] +
                                                num[d])
                                            printed.add(
                                                '(' + num[a] + sign[e] + num[b] + ')' + sign[f] + '(' + num[c] + sign[
                                                    g] +
                                                num[
                                                    d] + ')')
        if not printed:
            print('No result')
    else:
        print('Incorrect input type')

main()
