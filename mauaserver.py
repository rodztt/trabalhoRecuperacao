from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testes.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from model import *

@app.route('/')
def homepage():return '''TESTE HANNOI<br><br>route [/]:<br><br>\t\
	Rotas do servidor:<br>[<a href= \"http://localhost:5000/testes">/testes</a>]<br>\
	<br>[<a href= \"http://localhost:5000/medida/new">/teste/new</a>]<br>\
	<br>[<a href= \"http://localhost:5000/conjunto/new">/conjunto/new</a>]<br>\
	[<a href= \"http://localhost:5000/check_device/default">/check_device</a>]"'''
	

@app.route('/testes', methods=['GET'])
def testes_list():
	testes = []
	for i in Testes.query.all():
		print i.identificacao, i.movimentos
		testes.append({'id': i.id, 'identificacao': i.identificacao, 'movimentos': i.movimentos})

	return json.dumps(testes)


@app.route('/conjunto/new', methods=['POST'])
def teste_new():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	a = Testes()
	a.identificacao = p['identificacao']
	a.movimentos = p['movimentos']
	db.session.add(a)
	db.session.commit()

	return jsonify({'status:': True})


if __name__ == '__main__':
	app.run(debug=True)

