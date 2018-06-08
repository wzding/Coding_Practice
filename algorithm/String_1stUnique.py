def first_unique(s):
    import collections
    idx =[]
    for c,v in collections.Counter(s).iteritems():
        if v == 1:
            idx.append(c)
    if idx == []:
        unique_char =  None        
    else:
        unique_char = idx[0]
    return unique_char

print first_unique('aabbcdd123')
print first_unique('a')
print first_unique('112233')