def list_add(t):
    """ Variable Creator """
    list = []
    for int in range(0,8):
        tint = t + str(int)
        list.append(tint)
    print(', '.join(list))


list_add('t')
