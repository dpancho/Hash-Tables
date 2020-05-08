"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
# q = (1, 2, 3)

def f(x):
    return x * 4 + 6

r = [f(x) for x in q[-1::-1]]
# TODO: Implement me.

hash_sum, hash_min = {}, {}

for i in r:
    for j in r:
        hash_sum[(i,j)] = i + j
        hash_min[(i,j)] = i - j

for  k, v in hash_sum.items():
    for k2, v2 in hash_min.items():
        if v == v2:
            print(k , k2)

# for a in range(len(q)):
#     for b in range(len(q)):
#         key = (q[a], q[b])
#         key2= (q[b], q[a])
#         if key not in add_hashtable and key2 not in add_hashtable:
#             result = add(q[a], q[b])
#             add_hashtable[key] = result
#             print(q[a], "+", q[b], result)

# for c in range(len(q)):
#     for d in range(len(q)):
#         key = (q[c], q[d])
#         key2= (q[d], q[c])
#         if key not in sub_hashtable and key2 not in sub_hashtable:
#             result = subtract(q[c], q[d])
#             sub_hashtable[key] = result
#             print(q[c], "+", q[d], result)