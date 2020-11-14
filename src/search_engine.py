import numpy as ny
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import math

stop_words = set(stopwords.words('english'))

def stemming(sentence):
   
    ps = PorterStemmer()
    sentence = re.sub(r'[^\w\s]', '',sentence)
    words = word_tokenize(sentence) 
    hasil_stem = []
    for w in words: 
        hasil_stem.append(ps.stem(w))
    removed_sw_words = [word for word in hasil_stem if word not in stop_words]
    return removed_sw_words

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

def perkalian_dot(vektor1,vektor2) :
    hasil_dot = 0
    for i in range(length(vektor1)) :
        hasil_dot += (vektor1[i]*vektor2[i])
    return hasil_dot

def panjang_vektor(vektor) : 
    panjang = 0
    for i in range(length(vektor)) :
        panjang += vektor[i]*vektor[i]
    panjangvektor = math.sqrt(panjang)
    return(panjangvektor)

def cosine_similarity(vektor1,vektor2) :
    similarity = (perkalian_dot(vektor1,vektor2))/(panjang_vektor(vektor1)*panjang_vektor(vektor2))
    return(similarity)
    
