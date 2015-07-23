from mauaserver import db

class Conjuntos(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        contador        = db.Column(db.Integer)
        testes          = db.relationship('Testes',backref='conjuntos', lazy='dynamic')

class Testes(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	foreign_id      = db.Column(db.Integer, db.ForeignKey('conjuntos.id'))
	identificacao	= db.Column(db.String(100))
	movimentos	= db.Column(db.Integer)
