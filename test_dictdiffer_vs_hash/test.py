import json
import timeit
import hashlib
import functools
import dictdiffer
from collections import OrderedDict

with open("2016-05-17T05:01:39.764Z.json") as f:
    str1 = f.read()
    dict1 = json.loads(str1, object_pairs_hook=OrderedDict)

with open("2016-05-20T13:55:59.497Z.json") as f:
    str2 = f.read()
    dict2 = json.loads(str2, object_pairs_hook=OrderedDict)

def is_different1(str1, str2):
    hash1 = hashlib.md5(str1.encode('utf-8'))
    hash2 = hashlib.md5(str2.encode('utf-8'))
    return hash1.hexdigest() != hash2.hexdigest()

def is_different2(dict1, dict2):
    return dict1 != dict2

def is_different3(dict1, dict2):
    dict1_filtered = {k:v for k,v in dict1.items() if k != "timestamp"}
    dict2_filtered = {k:v for k,v in dict1.items() if k != "timestamp"}
    return dict1_filtered != dict2_filtered

def is_different4(dict1, dict2):
    hash1 = hashlib.md5(str(dict1).encode('utf-8'))
    hash2 = hashlib.md5(str(dict2).encode('utf-8'))
    return hash1.hexdigest() != hash2.hexdigest()

def is_different5(dict1, dict2):
    # create new dictionary
    dict1_filtered = {k:v for k,v in dict1.items() if k != "timestamp"}
    dict2_filtered = {k:v for k,v in dict1.items() if k != "timestamp"}
    hash1 = hashlib.md5(str(dict1).encode('utf-8'))
    hash2 = hashlib.md5(str(dict2).encode('utf-8'))
    return hash1.hexdigest() != hash2.hexdigest()

def is_different6(dict1, dict2):
    # mutate dictionary
    timestamp1 = dict1.pop('timestamp')
    timestamp2 = dict2.pop('timestamp')
    hash1 = hashlib.md5(str(dict1).encode('utf-8'))
    hash2 = hashlib.md5(str(dict2).encode('utf-8'))
    dict1['timestamp'] = timestamp1
    dict2['timestamp'] = timestamp2
    return hash1.hexdigest() != hash2.hexdigest()

def is_different7(dict1, dict2):
    return len(list(dictdiffer.diff(dict1, dict2, ignore=["timestamp"]))) == 0

is_different1_curried = functools.partial(is_different1, str1, str2)
is_different2_curried = functools.partial(is_different2, dict1, dict2)
is_different3_curried = functools.partial(is_different3, dict1, dict2)
is_different4_curried = functools.partial(is_different4, dict1, dict2)
is_different5_curried = functools.partial(is_different5, dict1, dict2)
is_different6_curried = functools.partial(is_different6, dict1, dict2)
is_different7_curried = functools.partial(is_different7, dict1, dict2)

print("is_different1", timeit.timeit(is_different1_curried, number=1000))
print("is_different2", timeit.timeit(is_different2_curried, number=1000))
print("is_different3", timeit.timeit(is_different3_curried, number=1000))
print("is_different4", timeit.timeit(is_different4_curried, number=1000))
print("is_different5", timeit.timeit(is_different5_curried, number=1000))
print("is_different5", timeit.timeit(is_different5_curried, number=1000))
print("is_different6", timeit.timeit(is_different6_curried, number=1000))
print("is_different7", timeit.timeit(is_different7_curried, number=1000))

"""
is_different1 0.09071078099077567
is_different2 0.0005728219985030591
is_different3 0.006166105013107881
is_different4 2.5271879339998122
is_different5 2.731813116988633
is_different5 2.4548248360224534
is_different6 2.627726652979618
is_different7 6.907549369992921
"""
