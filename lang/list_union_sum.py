l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

# intersection
inters = filter(lambda x: x in l1, l2)

# union
union = l1 + filter(lambda x: x not in l1, l2)

# get sum of list
reduce(lambda x, y: x+y, inters)

# define 2 dictionaries
d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
d2 = {'c' : 1, 'd' : 2, 'e' : 3, 'f' : 4}

# intersection of their keys
inters = filter(lambda x: x in d1.keys(), d2.keys())

# sum of product of their values
reduce(lambda x, y: x + y, [d1[z] * d2[z] for z in inters])

# all at once!
reduce(lambda x, y: x + y, [d1[z] * d2[z] for z in filter(lambda x: x in d1.
keys(), d2.keys())])


