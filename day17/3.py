def addiction(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs)
result = addiction(a=1)