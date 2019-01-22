def sortColors(a):
    if not a:
        return
    
    pl, pr = 0, len(a)-1
    i = 0
    while i <= pr:
        if a[i] == 0:
            a[pl], a[i] = a[i], a[pl]
            pl += 1
            i += 1
        elif a[i] == 1:
            i += 1
        else:
            a[pr], a[i] = a[i], a[pr]
            pr -= 1
