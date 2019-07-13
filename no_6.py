def func(op, n, d):
    assert 1 < n <= 1000
    val = ''

    for i in range(1, n+1):
        val += str(i)

    if op.upper() == "SUM":
        base = 0
        for i in d:
            base += int(val[i - 1])
        return base
    if op.upper() == "MUL":
        base = 1
        for i in d:
            base *= int(val[i - 1])
        return base
    if op.upper() == "SUB":
        base = 0
        for i in d:
            if i == d[0]:
                base += int(val[i - 1])
            else:
                base -= int(val[i - 1])
        return base
    if op.upper() == "DIV":
        base = 0
        for i in d:
            if i == d[0]:
                base += int(val[i - 1])
            else:
                base //= int(val[i - 1])
        return base

print(func("SUM", 20, [11, 13, 15]))
print(func("MUL", 20, [12, 15, 17]))