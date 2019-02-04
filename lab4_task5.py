import string
def stringoperation():
    myfile = open("emma.txt","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    for my in myfile:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    for key, value in histo.items():
        if(value == 20):
            print(key)

stringoperation()



