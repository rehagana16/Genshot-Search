import numpy as ny
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english'))

def stemming(sentence):
   
    ps = PorterStemmer()
    words = word_tokenize(sentence) 
    removed_sw_words = [word for word in words if word not in stop_words]
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

# Calculate similarity with cosine similarity
similarity = {}

for i in range(len(stemmed_sentence)) :
	if (ny.linalg.norm(x[i]) * ny.linalg.norm(vectorized_query) != 0)
		similarity[i] = ny.dot(vectorized_sentence[i]) / (ny.linalg.norm(vectorized_sentence[i]) * ny.linalg.norm(vectorized_query))
	else :
		similarity[i] = 0

# Sorting
sorted_similarity = sorted(similarity.items(), reverse = True)
            


    
