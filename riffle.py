def riffle(items,out=True):
    length=len(items)
    a=iter(items[:length//2])
    b=iter(items[length//2:])

    result=[]
    for x in range(length//2):
        if out:
            result.append(next(a))
            result.append(next(b))
        else:
            result.append(next(b))
            result.append(next(a))
    return result