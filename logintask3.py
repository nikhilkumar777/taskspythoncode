# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:15:52 2020

@author: user
"""

data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}

def slen(data):
    dict_len= {key: len(value) for key, value in data.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
    x=sorted_key_list[:5]
    skl=sorted(x, key=operator.itemgetter(0), reverse=False)
    y=skl+sorted_key_list[5:7]
    sorted_dict = [{item[0]: data[item [0]]} for item in y]
    return sorted_dict
print(slen(data)) 

  


