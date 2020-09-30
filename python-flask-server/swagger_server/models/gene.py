from app import db


class krp1(db.Model):
    __tablename__ = 'krp1'

    id = db.Column(db.String(20), nullable = False)
    URI = db.Column(db.String(200), nullable = False)
    graph = db.Column(db.String(200), nullable = False)
    keyword_reference = db.Column(db.String(50), nullable = False)
    belong_to_gene = db.Column(db.Integer, primary_key = True)
    type  = db.Column(db.Integer, nullable = False)

class tcp2(db.Model):
    __tablename__ = 'tcp2'

    id = db.Column(db.String(50), nullable = False)
    URI = db.Column(db.String(200), nullable = False)
    graph = db.Column(db.String(200), nullable = False)
    keyword_reference = db.Column(db.String(100), nullable = False)
    belong_to_gene = db.Column(db.Integer, primary_key = True)
    type  = db.Column(db.Integer, nullable = False)
