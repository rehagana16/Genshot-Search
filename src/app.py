# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,jsonify
import os  
import search_engine
import read_file                                     
app = Flask(__name__, template_folder='templates') 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

nama_file = []
isi_content = []
array_nama = []
list_content = []
key_all = []
key_query = []

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
		print(file)
		filename = file.filename
		destination = "/".join([target, filename])
		print(destination)
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
	return render_template("upload_complete.html", name = array_nama)

@app.route('/search',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
def search() : 
	result = []   
	word = ""
	similarity = []
	hasil = []
	if (request.method == "POST") :
		word = request.form.get("search")
		query_stemmed = search_engine.stemming(word)
		key_query = search_engine.make_key(query_stemmed)     
		for i in key_query : 
			key_all.append(i) 
		for x in range(search_engine.length(list_content)):
			vektor_result = search_engine.vectorizer(key_all,word)
			vektor_konten = search_engine.vectorizer(key_all,list_content[x])
			similarity.append(search_engine.cosine_similarity(vektor_result,vektor_konten))
			hasil.append([nama_file[x],list_content[x],similarity])
		if result:
			pass
	return render_template("search.html",result=hasil,key=key_all)

@app.route('/printkey', methods=["GET","POST"])
def printkey():
	hasil_table = []
	for x in  range(search_engine.length(list_content)):
		table_result = search_engine.vectorizer(key_query,list_content[x])
		hasil_table.append([key_query,table_result])
	return render_template("key.html", key=key_all, hasil=hasil_table)

if __name__ == '__main__':
   app.run(debug=True)
