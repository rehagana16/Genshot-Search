# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import os  
import search_engine                                     
app = Flask(__name__, template_folder='templates') 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods= ['POST'])
def upload() :
	target = os.path.join(APP_ROOT, 'pdf_database/')
	print(target)

	if not os.path.isdir(target) :
		os.mkdir(target)
	
	for file in request.files.getlist("file") :
		print(file)
		filename = file.filename
		destination = "/".join([target, filename])
		print(destination)
		file.save(destination)
		
	return render_template("upload_complete.html")

@app.route('/search',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
def search() : 
	result=[]   
	word =""
	if (request.method == "POST"):
         word = request.form.get("search")       
         result = search_engine.stemming(word) 
         if result:
	         pass
	return render_template("search.html",result=result,word=word)


if __name__ == '__main__':
   app.run(debug=True)

