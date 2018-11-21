#list_of_dic_unequal_len = [{'valueOfMeta': [u'2098916', u'2098915', u'2098914', u'2098913', u'2098912', u'2098911', u'2098910', u'2098909', u'2098908', u'2098907'], 'occurencesOfMeta': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'total': 10, 'name': u'sessionid'}, {'valueOfMeta': [u'127.0.0.1', u'20.20.20.20'], 'occurencesOfMeta': [1507, 1], 'total': 2, 'name': u'ip.src'}, {'valueOfMeta': [u'127.0.0.1', u'10.10.10.10'], 'occurencesOfMeta': [1507, 1], 'total': 2, 'name': u'ip.dst'}]

csv_list = list()
print("The list of dictionaries of unequal length is "+str(list_of_dic_unequal_len))

for item in list_of_dic_unequal_len:
    csv_list.append([item['name']] + item['valueOfMeta'])
    csv_list.append(['Meta Occurance'] + [str(item) for item in item['occurencesOfMeta']])
    
# This maps equal length dictionaries and skips the rest of the elements
list_tup = zip(*csv_list) 
print("The one on one mapping result "+str(list_tup))

# This maps all elements in dictionaries of unequal length and adds None to those elements which arent in the dictionary of lesser length
all_mapped_result = map(None, *csv_list) 
print("The one on one mapping without skipping any element result "+str(all_mapped_result))

# Replace None with empty string ''
list_of_mapping = [['' if ele is None else ele for ele in item] for item in all_mapped_result]
# Final result of list of lists having one to one mapping replacing None with empty string ''
print(list_of_mapping) 

# This can be used to make comma seperated list to insert the elements in CSV
DATA = '\n'.join(','.join(sub) for sub in list_of_mapping)
print(DATA) 
