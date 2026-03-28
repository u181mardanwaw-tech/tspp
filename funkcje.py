def f1(d):
    return tuple(d.keys())


def f2(l):
    for el in reversed(l):
        print(el)


def f3(l):
    result = []
    suma = 0

    for el in l:
        suma += el
        result.append(suma)

    print(result)
    return result


def f4(a1, a2):
    return set(a1) == set(a2)