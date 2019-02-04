import string

fp=open('emma.txt')
name=fp.read()
fp1=open('words.txt')
name1=fp1.read()

def print_book(book):
	mydict=dict()
	for line in book.split():
		word=line.strip(string.punctuation)
		if word not in mydict:
			mydict[word]=1
		else:
			mydict[word]+=1
	return mydict


def subtract(d1,d2):
        res=dict()
        for key in d1:
                if key not in d2:
                        res[key]=None
        return res

hist=print_book(name)
words=print_book(name1)
diff=subtract(hist,words)

print('The words in book that is not in words file are:')
for word in diff:
	print(word,sep='\n')













#	print('The different no of words in the book is:',len(mydict))
"""	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print(mylist)
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t') """

