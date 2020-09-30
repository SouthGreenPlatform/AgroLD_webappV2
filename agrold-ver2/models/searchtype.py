from app import db


class filters(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer(), nullable = False, primary_key = True)
    type = db.Column(db.String(20), nullable = False)

