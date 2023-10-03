#! /bin/python3

import re

#re_pattern = r'for'
#re_pattern_obj = re.compile(re_pattern)
#re_result = re_pattern_obj.match(to_search)
#print(re_result)

def re_search(re_pattern, to_search):
    re_pattern_obj = re.compile(re_pattern, re.IGNORECASE)
    if re_pattern_obj.finditer(to_search):
        found_instances = re_pattern_obj.finditer(to_search)
        for m in found_instances:
            print(m.start(), m.end(), m.group(0))
        return "found"
    else:
        return "Not found"

result = re_search("for", "Before")
print(result)

re_pattern = r'[a-zA-Z]'
re_pattern_obj = re.compile(re_pattern)
to_search = 'Canoe'

x = re_pattern_obj.findall(to_search)
print(x)
