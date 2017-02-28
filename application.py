#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, flash, redirect, url_for, render_template, session
app = Flask(__name__)
app.secret_key = 'F34TF$($e34D';
from fonctions import *
from numpy import *
from scipy import linalg

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/accueil')
def accueil_():
    return render_template('accueil.html')

@app.route('/gauss', methods=['POST', 'GET'])
def gauss():
	if request.method == 'POST': 
		n=int(request.form['ordre'])
		A = CreeMatCar(n);
		b=CreerListe(n)
		solution=CreerListe(n)
		for i in range (0,n):
			for j in range (0,n):
				A[i][j]=float(request.form["m"+str(i)+str(j)]);
			b[i]=float(request.form["c"+str(i)]);
		solution=solveSystGauss(A,b)
		return render_template('gauss.html',A=A, b=b,s=solution)
	if request.method == 'GET':
		return render_template('gauss.html')

@app.route('/lu', methods=['POST', 'GET'])
def lu():
	if request.method == 'POST': 
		n=int(request.form['ordre'])
		A = CreeMatCar(n);
		b=CreerListe(n)
		solution=CreerListe(n)
		for i in range (0,n):
			for j in range (0,n):
				A[i][j]=float(request.form["m"+str(i)+str(j)]);
			b[i]=float(request.form["c"+str(i)]);
		A=linalg.lu_factor(A)
		solution= linalg.lu_solve(A,b)
		return render_template('lu.html',A=A, b=b,s=solution)
	if request.method == 'GET':
		return render_template('lu.html')

@app.route('/cholesky', methods=['POST', 'GET'])
def cholesky():
	if request.method == 'POST': 
		n=int(request.form['ordre'])
		A = CreeMatCar(n);
		b=CreerListe(n)
		solution=CreerListe(n)
		for i in range (0,n):
			for j in range (0,n):
				A[i][j]=float(request.form["m"+str(i)+str(j)]);
			b[i]=float(request.form["c"+str(i)]);
		solution=solveSystCholesky(A,b)
		return render_template('cholesky.html',A=A, b=b,s=solution)
	if request.method == 'GET':
		return render_template('cholesky.html')

@app.route('/qr')
def qr():
	return render_template('qr.html')

@app.route('/documentation')
def documentation():
	return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
