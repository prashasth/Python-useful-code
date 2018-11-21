import re

list_of_dict = [{'ip.src.ad': 1, 'ip.dst':2}, {'ad.user':3, 'ad':4, 'ad.user.src':5}]
list_of_dict_camelCase = list()

callback = lambda x:x.group(0).upper()

for item in list_of_dict:
    keys = item.keys()
    values = item.values()
    keys = [re.sub('\.\w',callback,key).replace('.','') for key in keys]
    dict_result_camel = dict(zip(keys,values))
    list_of_dict_camelCase.append(dict_result_camel)

# Output - [{'ipDst': 2, 'ipSrcAd': 1}, {'adUser': 3, 'adUserSrc': 5, 'ad': 4}]
print(list_of_dict_camelCase)
