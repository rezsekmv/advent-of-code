
import re

def getCommon(list1, list2):
    return list(set(list1).intersection(list2))

def getNumbers(str):
    return [int(s) for s in re.findall(r'\b' + r'\d+' + r'\b', str)]

def getRegexp(str, regexp='^[a-zA-Z]+$'):
    return re.findall(regexp, str)

def getFirstRegexp(str, regexp='^[a-zA-Z]+$'):
    res = re.findall(regexp, str)
    if len(res) > 0:
        return res[0]
    else:
        return ''
