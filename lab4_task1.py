import string

fp=open('emma.txt')
name=fp.read()
for line in name.split():
	word=line.strip(string.punctuation)
	print(word.lower())

