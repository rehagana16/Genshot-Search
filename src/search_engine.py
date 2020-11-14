from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

def stemming(sentence):
   
    ps = PorterStemmer() 
    words = word_tokenize(sentence) 
    hasil_stem = []
    for w in words: 
        hasil_stem.append(ps.stem(w))
    return hasil_stem

def length(sentence) :
    count = 0
    for i in sentence : 
        count += 1
    return count

def search(list1,word) :
    found = False
    i = 0
    while ((found == False) and (i<length(list1))):
        if (list1[i] == word) :
            found = True
        else :
            i+=1
    if (found) : 
        return i
    else : 
        return -1

def make_key(isi) :
    key = []
    for i in (isi) :
        if (i not in key) :
            key.append(i)
    return key

def vectorizer(isi) :
    hasil_stem = stemming(isi)
    key = make_key(hasil_stem)
    jumlah = [0 for i in range(length(key))]
    for i in (stemming(isi)) :
        posisi = search(key,i)
        if (posisi != -1) :
            jumlah[posisi] += 1
    return jumlah
            
def read_file(filename) :
    file = open(filename,"r")
    content = my_file.read()
    content_list = content.split(",")
    file.close()
    print(content_list)

    
