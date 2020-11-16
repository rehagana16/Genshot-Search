# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,jsonify,redirect
from nltk.tokenize import word_tokenize
import os
import re  
import search_engine
import web_scraper                                     
app = Flask(__name__, template_folder='templates') 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

filename_scraping = []
content_scraping = []
nama_file = []
isi_content = []
array_nama = []
list_content = []
key_all = []



@app.route("/")
def index():
	return redirect("/web_scraping")

@app.route("/web_scraping", methods= ["GET","POST"])
def web_scraping() :
	web_scraper.web_scraping(filename_scraping,content_scraping)
	if filename_scraping: 	#kasus saat web scraping berhasil
		for file in range (len(filename_scraping)) :
			content = content_scraping[file]
			hasil_stem = search_engine.stemming(content)
			document_content = search_engine.vectorizer(search_engine.make_key(hasil_stem),content)
			array_nama.append([filename_scraping[file].rsplit('.',1)[0],document_content])
			nama_file.append(filename_scraping[file].rsplit('.',1)[0])
			list_content.append(content)
			key_content = search_engine.make_key(hasil_stem)
			for i in key_content : 
				key_all.append(i)
		return redirect('/search')
	else:		#kasus saat web scraping gagal
		print("No file delected.")
		return render_template("web_scraping.html", error_message = "Web scraping error. Try reloading the page.")

@app.route('/search',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
def search() : 
	result = []   
	similarity = []
	hasil = []
	hasil_table = []
	vector_table = []
	jumlah_kata = []
	kalimat_pertama = []
	input_query = []
	key_query_table = []
	word = ""
	if (request.method == "POST") :
		word = request.form.get("search")
		input_query.append(word)
		query_stemmed = search_engine.stemming(word)
		if query_stemmed :
			key_query = search_engine.make_key(query_stemmed)     
			for i in key_query : 
				key_all.append(i) 
				key_query_table.append(i)
			for x in range(search_engine.length(list_content)):
				vektor_result = search_engine.vectorizer(key_all,word)
				vektor_konten = search_engine.vectorizer(key_all,list_content[x])
				similarity.append(float(search_engine.cosine_similarity(vektor_result,vektor_konten)))
			nama_file1,list_content1,similarity1 = search_engine.sort(nama_file,list_content, similarity)
			for x in  range(search_engine.length(list_content1)):
				search_engine.hitung_jumlah_kata(list_content1[x],jumlah_kata)
				search_engine.ambil_kalimat_pertama(list_content1[x],kalimat_pertama)
			for x in range(search_engine.length(list_content)):
				hasil.append([nama_file1[x],jumlah_kata[x],kalimat_pertama[x],similarity1[x],list_content1[x]])
			table_result = search_engine.vectorizer(key_query_table,input_query[0])
			vector_table.append(table_result)
			hasil_table.append([key_query_table,table_result])
			for x in  range(search_engine.length(list_content)):
				table_result = search_engine.vectorizer(key_query_table,list_content[x])
				vector_table.append(table_result)
				hasil_table.append([key_query_table,table_result])
			if result:
				pass
		else :
			return render_template("search.html",error_message="No results found") 
	return render_template("search.html",result=hasil ,key=key_all, query = key_query_table,length = search_engine.length(vector_table),query_length = search_engine.length(key_query_table),vector = vector_table)

def printkey():
	hasil_table = []
	vector_table = []
	table_result = search_engine.vectorizer(key_query_table,input_query[0])
	vector_table.append(table_result)
	hasil_table.append([key_query_table,table_result])
	for x in  range(search_engine.length(list_content)):
		table_result = search_engine.vectorizer(key_query_table,list_content[x])
		vector_table.append(table_result)
		hasil_table.append([key_query_table,table_result])

@app.route('/document_details/<string:nama_dokumen>/<string:konten>', methods=["GET","POST"])
def document_details(nama_dokumen, konten):
	return render_template("document_details.html", nama_dokumen=nama_dokumen, konten=konten)

if __name__ == '__main__':
   app.run(debug=True)
