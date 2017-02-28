#/usr/bin/env python
# -*- coding:utf-8 -*-
#Ici on importe la bibliotheque flask ainsi que  l'objet request
from flask import Flask,request,redirect,url_for,render_template
app=Flask(__name__)

#definition des routes
@app.route('/')
def index():
	#on redirige vers la  page accueil 
	return render_template("index.html")

@app.route('/inverse',methods=['GET','POST'])
def inverse():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("inverse.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("inverse.html")


	

@app.route('/lu')
def lu():
	#on redirige vers la  page lu.html 
	return render_template("lu.html")

@app.route('/result',methods=['GET','POST'])
def result():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		return render_template("result.html",dimension=dimension,matrice=mat)
	#Si c la methode GET	
	if(request.method=='GET'): 
		return render_template("result.html")


app.run(debug= True)
