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
def homepage():return '''TESTE HANNOI By RTT <br><br>
	Rotas do servidor:<br>

	<br>Lista os testes: [<a href= \"http://localhost:5000/testes">/testes</a>]<br>\
	
	<br>Link para postar os testes: [<a href= \"http://localhost:5000/medida/new">/teste/new</a>]<br>\
		
	<br>Lista os conjuntos: [<a href= \"http://localhost:5000/conjuntos">/conjuntos</a>]<br>\
	
	'''
	

@app.route('/testes', methods=['GET'])
def testes_list():
	testes = []
	for i in Testes.query.all():
		print i.identificacao, i.movimentos
		testes.append({'id': i.id, 'foreign_id':i.foreign_id, 'identificacao': i.identificacao, 'movimentos': i.movimentos})

	return json.dumps(testes)


@app.route('/conjuntos', methods=['GET'])
def conjuntos_list():
	conjuntos = []
	for i in Conjuntos.query.all():
		print i.id, i.contador
		conjuntos.append({'id': i.id, 'contador':i.contador})

	return json.dumps(conjuntos)


@app.route('/conjunto/new', methods=['POST'])
def teste_new():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	b = p['contador']
	w=[]
	a = Conjuntos()
	a.contador=p['contador']
	db.session.add(a)
	for i in range(b):
                w.append('a'+str(i))
                w[i]= Testes()
	for i in range(b):
                w[i].identificacao = p['testes'][i]['identificacao'] 
                w[i].movimentos = p['testes'][i]['movimentos']
                db.session.add(w[i])        
        db.session.commit()

	return jsonify({'status:': True})


if __name__ == '__main__':
	app.run(debug=True)


