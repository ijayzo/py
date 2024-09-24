def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
	for key in copy:
		del dictionary[key]
	for key in copy:
		dictionary[copy[key]] = key
