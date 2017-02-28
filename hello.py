#! /usr/bin/python # -*- coding:utf-8 -*-
from flask import Flask,render_template,request
from rever import *
import math as m
from fonctions import *
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST']) 
def index():
	if request.method == 'POST': 
		msg=int(request.form['textfield'])
		L = uneMatrice(msg);
		M = uneMatrice(msg);
		i=0;
		for i in range (0,msg):
			for j in range (0,msg):
				x=((i*msg)+j);
				if request.form[str(x)]!="textfield":
					L[i][j]=float(request.form[str(x)]);
		M=inversion(L);
		return render_template('resultat.html')+"{f}".format(f=M)

	if (request.method == 'GET') and (request.args.get('x')=='7') :
			return render_template('lu.html')
	if (request.method == 'GET') and (request.args.get('x')=='8') :
			return render_template('bbt.html')
	if (request.method == 'GET') and (request.args.get('x')=='9') :
			return render_template('grad.html')


	if (request.method == 'GET') and (request.args.get('x')>0) and (request.args.get('x')!='3'):
			return render_template('momo.html')
	return render_template('template.html')

@app.route('/resultat', methods=['GET', 'POST']) 
def result():
	if request.method == 'POST': 
		msg=int(request.form['textfield'])
		A = CreeMatCar(msg);
		k=0
		arret=0
		i=0;
		for i in range (0,msg):
			for j in range (0,msg):
				x=((i*msg)+j);
				if request.form[str(x)]!="textfield":
					A[i][j]=float(request.form[str(x)]);
		msg=len(A)
		L=CreeMatCar(msg)
		while k!=msg and arret!=1:
			L[k][k]=1
			if A[k][k] !=0:
				for i in range(k+1,msg):
					L[i][k]=round((float(A[i][k])/float(A[k][k])),5)
				A=eliminationLU(k,A)
				k+=1
			else:
				arret=1
		if arret==0 and A[msg-1][msg-1]!=0:
			return render_template('resultatlu.html')+"{f}".format(f=L)
		else:
			return ("Cette matrice n'est pas factorisable en LU");

@app.route('/res', methods=['GET', 'POST'])
def res():
	if request.method == 'POST': 
		msg=int(request.form['textfield'])
		A=CreeMatCar(msg)
		i=0
		for i in range (0,msg):
			for j in range (0,msg):
				x=((i*msg)+j)
				if request.form[str(x)]!="textfield":
					A[i][j]=float(request.form[str(x)])
		B=CreeMatCar(msg)
		B[1][1]=round(m.sqrt(A[1][1]),2)
		for z in range (0,msg):
			B[1][z]=round((float)(A[1][z]/B[1][1]),2)
		"remplir les autres colonnes"
		for j in range(1,msg):
			B[j][j]=A[j][j]
			r=0
			for k in range(2,j):
				r=B[j][k]
				r=r*r
				B[j][j]-=(float)(r)
			B[j][j]= round(m.sqrt(B[j][j]),2)
			for i in range(j+1,n):
				B[i][j]=A[i][j]
				for k in range(j):
					B[i][j]=B[i][j]-(B[i][k]*B[j][k])
				B[i][j]=round(B[i][j]/B[j][j],2)
		return render_template('resultatbbt.html')+"{f}".format(f=B)

"""@app.route('/grad', methods=['GET', 'POST'])
def res():
	if request.method == 'POST':"""




def momo():
	return ("momo");


if __name__ == '__main__':    
	app.run(debug=True)