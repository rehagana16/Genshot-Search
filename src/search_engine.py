from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

def stemming(sentence):
   
    ps = PorterStemmer() 
    words = word_tokenize(sentence) 
    hasil_stem = []
    for w in words: 
        hasil_stem.append(ps.stem(w))
    return hasil_stem
