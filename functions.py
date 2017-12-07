import hashlib

#Ubersimple hashing function
def hash(array):
	strarray = str(array)
	input = ''.join(strarray)
	return hashlib.sha256(input.encode('utf-8')).hexdigest()
