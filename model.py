from mauaserver import db

class Testes(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	contador        = db.Column(db.Integer)      
	identificacao	= db.Column(db.String(100))
	movimentos	= db.Column(db.Integer)
