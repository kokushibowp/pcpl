def field(items, *args):
    length = len(args)
    assert length > 0
    response = []
    if(length == 1):
        for i in items:
            for j in args:
                if j in i:
                    if(i[j] != None):
                        response.append(i[j])
    else:
        for i in items:
            tmpdict = {}
            isFilled = False
            for j in args:
                if j in i:
                    if(i[j] != None):
                        tmpdict[j] = i[j]
                        isFilled = True
            if(isFilled):
                response.append(tmpdict)
    return response
    # Необходимо реализовать генератор 