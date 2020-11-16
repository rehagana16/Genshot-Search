# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,jsonify,redirect
from nltk.tokenize import word_tokenize
import os
import re  
import search_engine
import read_file                                     
app = Flask(__name__, template_folder='templates') 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

nama_file = []
isi_content = []
array_nama = []
list_content = []
key_all = []
key_query_table = []
input_query = []
jumlah_kata = []
kalimat_pertama = []


@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods= ['POST'])
def upload() :
	target = os.path.join(APP_ROOT, 'txt_database/')
	print(target)

	if not os.path.isdir(target) :
		os.mkdir(target)
	
	#document_array = {}
	for file in request.files.getlist("file") :
		if file :	#kasus saat upload file ada dipilih file untuk diupload
			filename = file.filename
			destination = "/".join([target, filename])
			file.save(destination)
			content = read_file.text_read(filename)
			hasil_stem = search_engine.stemming(content)
			document_content = search_engine.vectorizer(search_engine.make_key(hasil_stem),content)
			array_nama.append([filename.rsplit('.',1)[0],document_content])
			nama_file.append(filename.rsplit('.',1)[0])
			list_content.append(content)
			key_content = search_engine.make_key(hasil_stem)
			for i in key_content : 
				key_all.append(i)
	if file: 	#kasus saat upload file ada dipilih file untuk diupload
		return redirect('/search')
	else:		#kasus saat upload file tidak dipilih file apa-apa
		print("No file selected.")
		return render_template("upload.html", error_message = "No files selected")

@app.route('/search',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
def search() : 
	result = []   
	similarity = []
	hasil = []
	hasil_table = []
	vector_table = []
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

@app.route('/printkey', methods=["GET","POST"])
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
	return render_template("key.html", key=key_all, hasil=hasil_table, result = vector_table, 
							query = key_query_table, length = search_engine.length(vector_table),
							query_length = search_engine.length(key_query_table))

@app.route('/print_search_result', methods=["GET","POST"])
def print_search_result():
	for x in  range(search_engine.length(list_content)):
		search_engine.hitung_jumlah_kata(list_content[x],jumlah_kata)
		search_engine.ambil_kalimat_pertama(list_content[x],kalimat_pertama)
	return render_template("search_result.html", jumlah_kata=jumlah_kata, kalimat_pertama=kalimat_pertama)

@app.route('/document_details/<string:nama_dokumen>/<string:konten>', methods=["GET","POST"])
def document_details(nama_dokumen, konten):
	return render_template("document_details.html", nama_dokumen=nama_dokumen, konten=konten)

@app.route('/perihal') 
def perihal(): 
	return render_template("perihal.html")

if __name__ == '__main__':
   app.run(debug=True)
