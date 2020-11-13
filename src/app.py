# -*- coding: utf-8 -*-

from flask import Flask,render_template,request  
import search_engine                                     
app = Flask(__name__, template_folder='templates') 

@app.route('/',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
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