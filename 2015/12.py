from util import *
import json

doc = get_data()
pr(sum(getNumbers(doc)))

def sum_numbers_no_red(obj):
	if isinstance(obj, int):
		return obj
	elif isinstance(obj, list):
		return sum(sum_numbers_no_red(item) for item in obj)
	elif isinstance(obj, dict):
		if "red" in obj.values():
			return 0
		return sum(sum_numbers_no_red(value) for value in obj.values())
	else:
		return 0
		
js = json.loads(doc)
pr(sum_numbers_no_red(js))