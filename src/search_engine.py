import numpy as ny
import re
import nltk
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

def vectorizer(key,isi) :
	hasil_stem = stemming(isi)
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

def hitung_jumlah_kata(document_content, jumlah_kata) :
	array_kata = document_content.split()
	count_kata = 0
	for i in array_kata :
		count_kata += 1
	jumlah_kata.append(count_kata)

def ambil_kalimat_pertama(document_content, kalimat_pertama) :
	sentences = nltk.sent_tokenize(document_content)
	kalimat_pertama.append(sentences[0])

def sort (nama, content, similarity) :
	for i in range(length(similarity) -1) :
		for j in range(length(similarity)-1) : 
			if (similarity[j] < similarity[j+1]) :
				temp = similarity[j]
				similarity[j] = similarity[j+1]
				similarity[j+1] = temp
				temp2 = nama[j]
				nama[j] = nama[j+1]
				nama[j+1] = temp2
				temp3 = content[j]
				content[j] = content[j+1]
				content[j+1] = temp3
	return nama,content,similarity


